import os
import requests
import json
from datetime import datetime, timezone, timedelta
import logging

# 设置日志配置
logging.basicConfig(filename='log/output.log', level=logging.INFO)

def get_inactive_party_members():
    url = "https://habitica.com/api/v3/groups/party/members"
    response = requests.get(url, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 请求成功，解析响应内容
        data = []
        members = response.json()['data']
        for member in members:
            member_id = member['id']
            # 发送GET请求到获取成员详细信息的API端点
            member_response = requests.get(f'https://habitica.com/api/v3/members/{member_id}', headers=headers)
            if member_response.status_code == 200:
                last_login = member_response.json()['data']['auth']['timestamps']['updated']
                duration = calculate_duration(last_login)
                if duration >= time_limit:
                    data.append(member_id)
            else:
                logger.error(f"Error retrieving member details for {member_id}: {member_response.status_code}")

        return data
    else:
        # 请求失败，打印错误信息
        logger.error(f"Error: {response.status_code}")
        logger.error(response.text)

def remove_users_from_party(user_ids_to_remove, message):
    url = "https://habitica.com/api/v3/groups/party/members"

    for user_id in user_ids_to_remove:
        message_url = f"https://habitica.com/api/v3/user/{user_id}/messages"
        message_data = {
            "message": message
        }
        message_response = requests.post(message_url, headers=headers, json=message_data)
        
        if message_response.status_code == 200:
            logger.info(f"Message sent to user {user_id}.")
        else:
            logger.error(f"Failed to send message to user {user_id}: {message_response.json()}")

    for user_id in user_ids_to_remove:
        response = requests.delete(f"{url}/{user_id}", headers=headers)
        
        if response.status_code == 200:
            logger.info(f"User {user_id} has been removed from the party.")
        else:
            logger.error(f"Failed to remove user {user_id}: {response.json()}")

def calculate_duration(last_login_time_str):
    # 将字符串转换为datetime对象
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    # 将datetime对象设置为UTC时区
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    # 计算时间差
    duration = current_time - last_login_time

    return duration

def manage_habitica_party_members(message):
    remove_id_list = get_inactive_party_members(time_limit)
    remove_users_from_party(remove_id_list, message)

if __name__ == "__main__":
    logger.info("# " + os.environ["RUN_NUMBER"])
    time_limit = timedelta(days=5)
    message = "Sorry, you haven't been online for 5 days. We have decided to invite you out of the party."
    
    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }

    logger.info("Habitica 描述更新成功")