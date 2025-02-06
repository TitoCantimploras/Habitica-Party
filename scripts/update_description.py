import os
import requests
import json
from datetime import datetime, timezone
import logging
import time

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
        time.sleep(request_interval - elapsed_time)

    # 发送请求
    response = method(url, **kwargs)

    # 更新最后请求时间
    last_request_time = time.time()

    return response

def get_daily_sentence():
    response = rate_limited_request(requests.get, "https://sentence.iciba.com/?c=dailysentence&m=getTodaySentence")
    response.raise_for_status()  # 检查请求是否成功
    return response.json()

def get_habitica_party_data():
    url = "https://habitica.com/api/v3/groups/party/members"
    response = rate_limited_request(requests.get, url, headers=headers)

    if response.status_code == 200:
        data = []
        members = response.json()['data']
        for member in members:
            member_id = member['id']
            member_response = rate_limited_request(requests.get, f'https://habitica.com/api/v3/members/{member_id}', headers=headers)
            if member_response.status_code == 200:
                last_login = member_response.json()['data']['auth']['timestamps']['updated']
                duration = calculate_duration(last_login)
                since_last_login = format_duration(duration)
                data.append({"name": member['profile']['name'], "last_login": last_login, "duration": duration, "since_last_login": since_last_login})
            else:
                logging.error(f"获取成员 {member_id} 的详细信息时出错: {member_response.status_code}")

            time.sleep(1)  # 在每次请求之间添加延迟

        return data
    else:
        logging.error(f"请求失败: {response.status_code}")
        logging.error(response.text)

def calculate_duration(last_login_time_str):
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    current_time = datetime.now(timezone.utc)
    duration = current_time - last_login_time

    return duration

def format_duration(duration):
    days = duration.days
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    
    time_parts = [f"{value}{unit}" for value, unit in 
                  zip([days, hours, minutes], ['d', 'h', 'm']) if value > 0]

    if time_parts == []:
        return "just now"
    
    return ' '.join(time_parts)

def format_current_time():
    time_str = current_time.strftime('%m-%d %I:%M %p, %Z')
    return time_str

def update_habitica_description(content, translation, members_str, time_str):
    url = "https://habitica.com/api/v3/groups/party"
    with open("Markdown_document/brief_description.md", "r") as f:
        template = f.read()
    description = template.format(content=content, translation=translation, members_str=members_str, time_str=time_str)
    data = {"description": description}

    response = rate_limited_request(requests.put, url, headers=headers, json=data)
    response.raise_for_status()  # 检查请求是否成功

if __name__ == "__main__":
    logging.basicConfig(filename='log/output.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("# " + os.environ["RUN_NUMBER"])
    current_time = datetime.now(timezone.utc)

    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }
    daily_sentence = get_daily_sentence()
    content = daily_sentence['content']
    translation = daily_sentence['note']

    members_list = sorted(get_habitica_party_data(), key=lambda x: x['duration'])
    members_str = '\n\n'.join(
        f"{index + 1}. {item['name']}:  {item['since_last_login']}" for index, item in enumerate(members_list)
    )

    time_str = format_current_time()

    update_habitica_description(content, translation, members_str, time_str)
    logging.info("队伍描述更新成功")