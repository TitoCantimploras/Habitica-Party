import os
import requests
import json
from datetime import datetime, timezone

def get_daily_sentence():
    response = requests.get("https://sentence.iciba.com/?c=dailysentence&m=getTodaySentence")
    response.raise_for_status()  # 检查请求是否成功
    return response.json()

def get_habitica_party_data():
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
                last_login = member_response.json()['data']['auth']['timestamps']['loggedin']
                duration = calculate_duration(last_login)
                since_last_login = format_duration(duration)
                # 解析成员的最后上线时间
                data.append({"name": member['profile']['name'], "last_login": last_login, "duration": duration, "since_last_login": since_last_login})
            else:
                print(f"Error retrieving member details for {member_id}: {member_response.status_code}")

        return data
    else:
        # 请求失败，打印错误信息
        print(f"Error: {response.status_code}")
        print(response.text)

def calculate_duration(last_login_time_str):
    # 将字符串转换为datetime对象
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    # 将datetime对象设置为UTC时区
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    # 获取当前UTC时间
    current_time = datetime.now(timezone.utc)
    # 计算时间差
    duration = current_time - last_login_time

    return duration

def format_duration(duration):
    # 计算天数、小时数、分钟数和秒数
    days = duration.days
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60
    
    # 使用列表推导式构建非零时间单位的字符串
    time_parts = [f"{value}{unit}" for value, unit in 
                  zip([days, hours, minutes, seconds], ['d', 'h', 'm', 's']) if value > 0]
    
    # 将所有非零的时间单位连接成一个字符串
    return ' '.join(time_parts)

def format_current_time():
    current_time = datetime.now(timezone.utc)
    time_str = current_time.strftime('%M-%d &H:&M:&S')

    return time_str

def update_habitica_description(time, content, translation, members_str):
    url = "https://habitica.com/api/v3/groups/party"
    description = f"### 每日一言 · Daily Sentence 🌹\n\n###### {time}\n\n{content}\n\n{translation}\n\n### 最后签到时间 · Last Check-In Time\n\n{members_str}\n\n#### Want to learn more about the party's purpose, rules, and other information? [Click here!](https://github.com/Delta-Water/Habitica-Party/blob/main/party_description.md)"
    data = {"description": description}

    response = requests.put(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # 检查请求是否成功
    return response.json()

if __name__ == "__main__":
    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }
    daily_sentence = get_daily_sentence()
    time = format_current_time()
    content = daily_sentence['content']
    translation = daily_sentence['note']

    members_list = sorted(get_habitica_party_data(), key=lambda x: x['duration'])
    members_str = '\n\n'.join(
        f"{index + 1}. {item['name']}:  {item['since_last_login']} ago" for index, item in enumerate(members_list)
    )

    update_habitica_description(time, content, translation, members_str)
    print("Habitica 描述更新成功")