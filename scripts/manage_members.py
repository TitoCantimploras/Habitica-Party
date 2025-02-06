import os
import requests
import json
from datetime import datetime, timezone, timedelta
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

def get_inactive_party_members(time_limit):
    url = "https://habitica.com/api/v3/groups/party/members"
    response = rate_limited_request(requests.get, url, headers=headers)

    if response.status_code == 200:
        data = []
        members = response.json()['data']
        for member in members:
            member_id = member['id']
            time.sleep(1)  # 这里可以根据API的限制调整

            member_response = rate_limited_request(requests.get, f'https://habitica.com/api/v3/members/{member_id}', headers=headers)
            if member_response.status_code == 200:
                last_login = member_response.json()['data']['auth']['timestamps']['updated']
                duration = calculate_duration(last_login)
                if duration >= time_limit:
                    data.append(member_id)
            else:
                logging.error(f"获取成员 {member_id} 的详细信息时出错: {member_response.status_code}")

        return data
    else:
        logging.error(f"错误: {response.status_code}")
        logging.error(response.text)

def remove_users_from_party(user_ids_to_remove, message):
    url = "https://habitica.com/api/v3/groups/party/members"

    for user_id in user_ids_to_remove:
        message_url = f"https://habitica.com/api/v3/user/{user_id}/messages"
        message_data = {
            "message": message
        }
        message_response = rate_limited_request(requests.post, message_url, headers=headers, json=message_data)
        
        if message_response.status_code == 200:
            logging.info(f"已向用户 {user_id} 发送消息。")
        else:
            logging.error(f"向用户 {user_id} 发送消息失败: {message_response.json()}")

    for user_id in user_ids_to_remove:
        response = rate_limited_request(requests.delete, f"{url}/{user_id}", headers=headers)
        
        if response.status_code == 200:
            logging.info(f"用户 {user_id} 已从队伍中移除。")
        else:
            logging.error(f"移除用户 {user_id} 失败: {response.json()}")

def send_invite(id_list):
    url = "https://habitica.com/api/v3/groups/party/invite"
    data = {"uuids": id_list}
    response = rate_limited_request(requests.post, url, json=data, headers=headers)
    if response.status_code == 200:
        logging.info(f"已向 {id_list} 发送邀请。")
    else:
        logging.error(f"邀请用户时出错: {response.status_code}, {response.text}")

def search_and_invite_users():
    url = "https://habitica.com/api/v3/looking-for-party"
    response = rate_limited_request(requests.get, url, headers=headers)
    if response.status_code == 200:
        groups = response.json().get('data', [])
        id_list = [group['_id'] for group in groups]
        send_invite(id_list)
    else:
        logging.error(f"获取队伍时出错: {response.status_code}, {response.text}")

def calculate_duration(last_login_time_str):
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    current_time = datetime.now(timezone.utc)
    duration = current_time - last_login_time
    return duration

def manage_habitica_party_members(message):
    remove_id_list = get_inactive_party_members(time_limit)
    remove_users_from_party(remove_id_list, message)
    search_and_invite_users()

if __name__ == "__main__":
    logging.basicConfig(filename='log/output.log', level=logging.INFO)

    logging.info("# " + os.environ["RUN_NUMBER"])
    time_limit = timedelta(days=5)
    message = "I'm sorry, but we've decided to remove you from the party because you haven't been online for 5 days."

    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }

    manage_habitica_party_members(message)

    logging.info("队伍自动管理任务执行成功")