import os
import requests
import json
from datetime import datetime, timezone, timedelta
import logging

def get_inactive_party_members(time_limit):
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
                # 如果用户不活跃超过设定的时间限制，则添加到待移除列表
                if duration >= time_limit:
                    data.append(member_id)
            else:
                logging.error(f"获取成员 {member_id} 的详细信息时出错: {member_response.status_code}")

            time.sleep(1)  # 在每次请求之间添加延迟


        return data
    else:
        # 请求失败，打印错误信息
        logging.error(f"错误: {response.status_code}")
        logging.error(response.text)

def remove_users_from_party(user_ids_to_remove, message):
    url = "https://habitica.com/api/v3/groups/party/members"

    for user_id in user_ids_to_remove:
        # 发送消息给待移除的用户
        message_url = f"https://habitica.com/api/v3/user/{user_id}/messages"
        message_data = {
            "message": message
        }
        message_response = requests.post(message_url, headers=headers, json=message_data)
        
        if message_response.status_code == 200:
            logging.info(f"已向用户 {user_id} 发送消息。")
        else:
            logging.error(f"向用户 {user_id} 发送消息失败: {message_response.json()}")

    for user_id in user_ids_to_remove:
        # 从队伍中移除用户
        response = requests.delete(f"{url}/{user_id}", headers=headers)
        
        if response.status_code == 200:
            logging.info(f"用户 {user_id} 已从队伍中移除。")
        else:
            logging.error(f"移除用户 {user_id} 失败: {response.json()}")

def send_invite(id_list):
    url = "https://habitica.com/api/v3/groups/party/invite"
    data = {"uuid": id_list}
    # 发送邀请请求
    response = requests.post(url, json=data, headers=headers)  # 改为POST请求
    if response.status_code == 200:
        logging.info(f"已向 {id_list} 发送邀请。")
    else:
        logging.error(f"邀请用户时出错: {response.status_code}, {response.text}")

def search_and_invite_users():
    url = "https://habitica.com/api/v3/looking-for-party"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        groups = response.json().get('data', [])
        # 提取用户ID
        id_list = [group['_id'] for group in groups]
        send_invite(id_list)
    else:
        logging.error(f"获取队伍时出错: {response.status_code}, {response.text}")

def calculate_duration(last_login_time_str):
    # 将字符串转换为datetime对象
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    # 将datetime对象设置为UTC时区
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    # 获取当前时间
    current_time = datetime.now(timezone.utc)
    # 计算时间差
    duration = current_time - last_login_time

    return duration

def manage_habitica_party_members(message):
    # 获取不活跃的成员ID列表
    remove_id_list = get_inactive_party_members(time_limit)
    # 移除不活跃的用户
    remove_users_from_party(remove_id_list, message)
    # 搜索并邀请新用户
    search_and_invite_users()

if __name__ == "__main__":
    # 设置日志配置
    logging.basicConfig(filename='log/output.log', level=logging.INFO)

    logging.info("# " + os.environ["RUN_NUMBER"])
    time_limit = timedelta(days=5)  # 设置不活跃时间限制为5天+-
    message = "I'm sorry, but we've decided to remove you from the party because you haven't been online for 5 days."

    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }

    # 管理Habitica队伍成员
    manage_habitica_party_members(message)

    logging.info("队伍自动管理任务执行成功")