import os

import requests
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN")
# AUTH_TOKEN = input("Введите токен: ")
HEADERS = {'Authorization': f'Bearer {AUTH_TOKEN}'}


def get_account_id():
    """Получение id организации"""

    url = "https://dev-100-api.huntflow.dev/accounts"
    response = requests.get(url, headers=HEADERS)
    return response.json()["items"][0]["id"]


ORGANIZATION_ID = get_account_id()

ADD_CANDIDATE_URL = f"https://dev-100-api.huntflow.dev/account/{ORGANIZATION_ID}/applicants"
GET_VACANCIES_ID_URL = f"https://dev-100-api.huntflow.dev/account/{ORGANIZATION_ID}/vacancies"
GET_STATUSES_ID_URL = f"https://dev-100-api.huntflow.dev/account/{ORGANIZATION_ID}/vacancy/statuses"
UPLOAD_FILE_URL = f"https://dev-100-api.huntflow.dev/account/{ORGANIZATION_ID}/upload"
