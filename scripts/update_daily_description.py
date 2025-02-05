import os
import requests
import json

def get_daily_sentence():
    response = requests.get("https://sentence.iciba.com/?c=dailysentence&m=getTodaySentence")
    response.raise_for_status()  # 检查请求是否成功
    return response.json()

def update_habitica_description(content, translation):
    url = "https://habitica.com/api/v3/groups/party"
    headers = {
        "x-api-user": os.environ["HABITICA_USER_ID"],
        "x-api-key": os.environ["HABITICA_API_KEY"],
        "Content-Type": "application/json"
    }
    description = f"""
    ### 每日一言 · Daily Sentence 🌹
    
    {content}
    
    {translation}
    
    #### Want to learn more about the party's purpose, rules, and other information? [Click here!](https://github.com/Delta-Water/Habitica-Party/blob/main/README.md)
    """
    data = {"description": description}
    
    response = requests.put(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # 检查请求是否成功
    return response.json()

if __name__ == "__main__":
    daily_sentence = get_daily_sentence()
    content = daily_sentence['content']
    translation = daily_sentence['note']
    
    update_habitica_description(content, translation)
    print("Habitica 描述更新成功")
