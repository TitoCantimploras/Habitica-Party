import os
import requests
import json
from datetime import datetime, timezone
import logging
import time
from requests.exceptions import RequestException

# 设置日志
logging.basicConfig(filename='log/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 全局变量
last_request_time = 0
request_interval = 1  # 默认请求间隔为1秒

def rate_limited_request(method, url, **kwargs):
    global last_request_time
    global request_interval

    # 计算当前时间与上次请求的时间差
    current_time = time.time()
    elapsed_time = current_time - last_request_time

    # 如果时间差小于请求间隔，则等待
    if elapsed_time < request_interval:
        wait_time = request_interval - elapsed_time
        logging.debug(f"Rate limiting active, waiting for {wait_time:.2f} seconds.")
        time.sleep(wait_time)

    # 发送请求
    try:
        response = method(url, **kwargs)
        response.raise_for_status()  # 检查请求是否成功
    except RequestException as e:
        logging.error(f"Request to {url} failed: {e}")
        return None

    # 更新最后请求时间
    last_request_time = time.time()
    return response

def get_daily_sentence():
    url = "https://sentence.iciba.com/?c=dailysentence&m=getTodaySentence"
    response = rate_limited_request(requests.get, url)
    if response:
        return response.json()
    else:
        return {}

def get_habitica_party_data(headers):
    url = "https://habitica.com/api/v3/groups/party/members"
    response = rate_limited_request(requests.get, url, headers=headers)

    if response and response.status_code == 200:
        data = []
        members = response.json().get('data', [])
        for member in members:
            member_data = get_member_details(member, headers)
            if member_data:
                data.append(member_data)
        return data
    else:
        logging.error(f"Failed to get party data: {response.status_code if response else 'No response'}")
        return []

def get_member_details(member, headers):
    member_id = member['id']
    url = f'https://habitica.com/api/v3/members/{member_id}'
    member_response = rate_limited_request(requests.get, url, headers=headers)
    if member_response and member_response.status_code == 200:
        member_details = member_response.json().get('data', {})
        last_login = member_details['auth']['timestamps']['updated']
        duration = calculate_duration(last_login)
        since_last_login = format_duration(duration)
        return {"name": member['profile']['name'], "last_login": last_login, "duration": duration, "since_last_login": since_last_login}
    else:
        logging.error(f"Failed to get details for member {member_id}: {member_response.status_code if member_response else 'No response'}")
        return None

def calculate_duration(last_login_time_str):
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    current_time = datetime.now(timezone.utc)
    return current_time - last_login_time

def format_duration(duration):
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    time_parts = []
    if days:
        time_parts.append(f"{days}d")
    if hours:
        time_parts.append(f"{hours}h")
    if minutes:
        time_parts.append(f"{minutes}m")
    
    return ' '.join(time_parts) if time_parts else "just now"

def format_current_time():
    return datetime.now(timezone.utc).strftime('%m-%d %I:%M %p, %Z')

def update_party_description(content, translation, members_str, time_str, headers):
    url = "https://habitica.com/api/v3/groups/party"
    try:
        with open("Markdown_document/brief_description.md", "r") as f:
            template = f.read()
        description = template.format(content=content, translation=translation, members_str=members_str, time_str=time_str)
        data = {"description": description}

        response = rate_limited_request(requests.put, url, headers=headers, json=data)
        if response:
            logging.info("Party description updated successfully.")
        else:
            logging.error("Failed to update party description.")
    except Exception as e:
        logging.error(f"An error occurred while updating the party description: {e}")

def main():
    logging.info(f"# Run number: {os.environ['RUN_NUMBER']}")
    current_time = datetime.now(timezone.utc)

    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }

    daily_sentence = get_daily_sentence()
    content = daily_sentence.get('content', '')
    translation = daily_sentence.get('note', '')

    members_list = sorted(get_habitica_party_data(headers), key=lambda x: x['duration'])
    members_str = '\n\n'.join(
        f"{index + 1}. {item['name']}:  {item['since_last_login']}" for index, item in enumerate(members_list)
    )

    time_str = format_current_time()

    update_party_description(content, translation, members_str, time_str, headers)

if __name__ == "__main__":
    main()
