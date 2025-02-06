import os
import requests
import json
from datetime import datetime, timezone, timedelta
import logging
import time

logging.basicConfig(filename='log/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

last_request_time = 0
request_interval = 1
    
time_limit = timedelta(days=5)
message = "I'm sorry, but we've decided to remove you from the party because you haven't been online for 5 days."

headers = {
    "x-api-user": os.environ["HABITICA_USER_ID"],
    "x-api-key": os.environ["HABITICA_API_KEY"],
    "Content-Type": "application/json"
}
    
with open("Markdown_document/new_members.md", "r") as f:
    template = f.read()

def rate_limited_request(method, url, **kwargs):
    global last_request_time
    wait_time = max(0, request_interval - (time.time() - last_request_time))
    if wait_time > 0:
        logging.debug(f"Rate limit enforced, waiting for {wait_time:.2f} seconds.")
        time.sleep(wait_time)
    response = method(url, **kwargs)
    last_request_time = time.time()
    return response

def get_json_response(response):
    try:
        return response.json()
    except json.JSONDecodeError:
        logging.error("Invalid JSON response received.")
        return None

def log_response_error(response, action):
    logging.error(f"{action} failed: Status code {response.status_code}, Response: {response.text}")

def get_inactive_party_members(time_limit):
    url = "https://habitica.com/api/v3/groups/party/members"
    response = rate_limited_request(requests.get, url, headers=headers)
    if response.status_code == 200:
        data = []
        members = get_json_response(response).get('data', [])
        for member in members:
            member_id = member['id']
            member_response = rate_limited_request(requests.get, f'https://habitica.com/api/v3/members/{member_id}', headers=headers)
            if member_response.status_code == 200:
                member_data = get_json_response(member_response).get('data', {})
                last_login = member_data['auth']['timestamps']['updated']
                if calculate_duration(last_login) >= time_limit:
                    data.append(member_id)
            else:
                log_response_error(member_response, f"Fetching details for member {member_id}")
        return data
    else:
        log_response_error(response, "Fetching party members")
        return []

def remove_users_from_party(user_ids_to_remove):
    url = "https://habitica.com/api/v3/groups/party/members"
    for user_id in user_ids_to_remove:
        send_message_to_user(user_id)
        response = rate_limited_request(requests.delete, f"{url}/{user_id}", headers=headers)
        if response.status_code == 200:
            logging.info(f"User {user_id} has been removed from the party.")
        else:
            log_response_error(response, f"Removing user {user_id} from the party")

def send_message_to_user(user_id):
    message_url = f"https://habitica.com/api/v3/user/{user_id}/messages"
    message_data = {"message": message}
    response = rate_limited_request(requests.post, message_url, headers=headers, json=message_data)
    if response.status_code == 200:
        logging.info(f"Message sent to user {user_id}.")
    else:
        log_response_error(response, f"Sending message to user {user_id}")

def send_invite(id_list, name_list):
    url = "https://habitica.com/api/v3/groups/party/invite"
    data = {"uuids": id_list}
    response = rate_limited_request(requests.post, url, json=data, headers=headers)
    if response.status_code == 200:
        id_str = '\n\n'.join([f"- [{name}](https://habitica.com/profile/{id})" for name, id in zip(name_list, id_list)])
        message = template.format(list=id_str)
        send_party_chat(message)
        logging.info(f"Invitations sent to {name_list}.")
    else:
        log_response_error(response, "Sending invitations")

def send_party_chat(message):
    url = "https://habitica.com/api/v3/groups/party/chat"
    data = {"message": message}
    response = rate_limited_request(requests.post, url, json=data, headers=headers)
    if response.status_code == 200:
        logging.info(f"Party chat message sent: {message}.")
    else:
        log_response_error(response, "Sending party chat message")

def search_and_invite_users():
    url = "https://habitica.com/api/v3/looking-for-party"
    response = rate_limited_request(requests.get, url, headers=headers)
    if response.status_code == 200:
        groups = get_json_response(response).get('data', [])
        id_list = [group['_id'] for group in groups]
        name_list = [group['auth']['local']['username'] for group in groups]
        if id_list:
            send_invite(id_list, name_list)
    else:
        log_response_error(response, "Fetching users looking for party")

def calculate_duration(last_login_time_str):
    last_login_time = datetime.strptime(last_login_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    last_login_time = last_login_time.replace(tzinfo=timezone.utc)
    current_time = datetime.now(timezone.utc)
    return current_time - last_login_time

def main():
    logging.info(f"# {os.environ['RUN_NUMBER']}")
    remove_id_list = get_inactive_party_members(time_limit)
    if remove_id_list:
        remove_users_from_party(remove_id_list)
    search_and_invite_users()
    logging.info("Habitica party management script completed successfully.")

if __name__ == "__main__":
    main()
