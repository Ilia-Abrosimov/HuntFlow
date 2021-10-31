import os
from typing import Dict, Any

import requests
from pprint import pprint
from dotenv import load_dotenv


load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# def get_me():
#     url = "https://dev-100-api.huntflow.dev/me"
#     headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
#     response = requests.get(url, headers=headers)
#     return response.json()
#
#
# pprint(get_me())

mydict = {'comments': 'Очень дорогой',
          'first_name': 'Александр',
          'last_name': 'Пушкин',
          'money': '100500',
          'position': 'Frontend-разработчик',
          'status': 'Отказ'}


def add_candidate(cv: Dict[str, Any]):
    url = "https://dev-100-api.huntflow.dev/account/2/applicants"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    data = {}
    data["last_name"] = cv.get("last_name")
    data["first_name"] = cv.get("first_name")
    if cv.get("middle_name") is not None:
        data["middle_name"] = cv.get("middle_name")
    data["position"] = cv.get("position")
    data["money"] = cv.get("money")
    data["externals"] = [
        {
            "auth_type": "NATIVE",
            "files": [
                {
                    "id": 4
                }
            ],
        }
    ]

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# print(add_candidate(mydict))


def get_vacancies_ids(cv: Dict[str, Any]):
    url = "https://dev-100-api.huntflow.dev/account/2/vacancies"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    response = requests.get(url, headers=headers)
    vacancies = response.json()["items"]
    for vacancy in vacancies:
        if cv.get("position") == vacancy.get("position"):
            return vacancy.get("id")


def get_statuses_ids(cv: Dict[str, Any]):
    url = "https://dev-100-api.huntflow.dev/account/2/vacancy/statuses"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    response = requests.get(url, headers=headers)
    statuses = response.json()["items"]
    for status in statuses:
        if cv.get("status") == status.get("name"):
            return status.get("id")


def upload_file():
    url = "https://dev-100-api.huntflow.dev/account/2/upload"
    files = {'file': ('Пушкин Александр', open('Frontend-разработчик/Танский Михаил.pdf', 'rb'), 'application/pdf')}
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}',
               'X-File-Parse': 'True'}
    response = requests.post(url, headers=headers, files=files)
    return response.json()


def add_candidate_at_vacancy():
    url = "https://dev-100-api.huntflow.dev/account/2/applicants/1170/vacancy"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    data = {
        "vacancy": get_vacancies_ids(mydict),
        "status": get_statuses_ids(mydict),
        "files": {
            "id": 4
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

print(add_candidate_at_vacancy())



