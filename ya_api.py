import json
import os
import requests
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
token = os.getenv('token_ya')

apiurl = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': token}


def create_folder(folder_name):
    params = {'path': folder_name}
    result = requests.put(apiurl, headers=headers, params=params)
    return result.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    result = requests.get(apiurl, headers=headers, params=params)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        return res_dict.get('type')


if __name__ == '__main__':
    print(create_folder('new_test'))
    print(get_folder_info('new_test'))