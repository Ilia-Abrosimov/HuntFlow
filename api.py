import os
from typing import Dict, Any
from parse_base import parsing_base
import requests
from pprint import pprint
from dotenv import load_dotenv


load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN")


mydict = {'comments': 'Очень дорогой',
          'first_name': 'Александр',
          'last_name': 'Пушкин',
          'money': '100500',
          'position': 'Frontend-разработчик',
          'status': 'Отказ'}


def add_candidate(cv: Dict[str, Any], file_id: int):
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
                    "id": file_id
                }
            ],
        }
    ]

    response = requests.post(url, headers=headers, json=data)
    candidate_id = response.json()["id"]
    return candidate_id


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
    file_id = response.json()["id"]
    return file_id


def add_candidate_at_vacancy(candidate_id: int, vacancy_id: int, status_id: int, file_id: int):
    url = f"https://dev-100-api.huntflow.dev/account/2/applicants/{candidate_id}/vacancy"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    data = {
        "vacancy": vacancy_id,
        "status": status_id,
        "files": {
            "id": file_id
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


data = parsing_base()

for candidate in data:
    file_id = upload_file()
    candidate_id = add_candidate(candidate, file_id)
    vacancy_id = get_vacancies_ids(candidate)
    status_id = get_statuses_ids(candidate)
    add_candidate_at_vacancy(candidate_id, vacancy_id, status_id, file_id)



