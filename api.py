import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from parse_base import parsing_base

load_dotenv()

# AUTH_TOKEN = os.getenv("AUTH_TOKEN")


def add_candidate(cv: Dict[str, Any], info_from_file: Dict[str, Any], AUTH_TOKEN):
    url = "https://dev-100-api.huntflow.dev/account/2/applicants"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    data = {}
    data["last_name"] = cv.get("last_name")
    data["first_name"] = cv.get("first_name")
    if cv.get("middle_name") is not None:
        data["middle_name"] = cv.get("middle_name")
    data["position"] = cv.get("position")
    data["money"] = cv.get("money")
    if info_from_file.get("fields")["phones"] is not None:
        data["phone"] = info_from_file.get("fields")["phones"][0]
    if info_from_file.get("fields")["email"] is not None:
        data["email"] = info_from_file.get("fields")["email"]
    if info_from_file.get("fields")["experience"][0]["company"] is not None:
        data["company"] = info_from_file.get("fields")["experience"][0]["company"]
    if info_from_file.get("fields")["birthdate"] is not None:
        data["birthday_day"] = info_from_file.get("fields")["birthdate"]["day"]
        data["birthday_month"] = info_from_file.get("fields")["birthdate"]["month"]
        data["birthday_year"] = info_from_file.get("fields")["birthdate"]["year"]
    if info_from_file.get("photo")["id"] is not None:
        data["photo"] = info_from_file.get("photo")["id"]
    data["externals"] = [
        {
            "data": {
                "body": info_from_file.get("text")},
            "auth_type": "NATIVE",
            "files": [
                {
                    "id": info_from_file["id"]
                }
            ],
        }
    ]
    response = requests.post(url, headers=headers, json=data)
    candidate_id = response.json()["id"]
    return candidate_id


def get_vacancies_ids(cv: Dict[str, Any], AUTH_TOKEN):
    url = "https://dev-100-api.huntflow.dev/account/2/vacancies"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    response = requests.get(url, headers=headers)
    vacancies = response.json()["items"]
    for vacancy in vacancies:
        if cv.get("position") == vacancy.get("position"):
            return vacancy.get("id")


def get_statuses_ids(cv: Dict[str, Any], AUTH_TOKEN):
    url = "https://dev-100-api.huntflow.dev/account/2/vacancy/statuses"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    response = requests.get(url, headers=headers)
    statuses = response.json()["items"]
    for status in statuses:
        if cv.get("status") == status.get("name"):
            return status.get("id")


def upload_file(cv: Dict[str, Any], AUTH_TOKEN):
    url = "https://dev-100-api.huntflow.dev/account/2/upload"
    path = cv.get("file_path")
    full_name = cv.get("full_name")
    files = {'file': (full_name, open(path, 'rb'), 'application/pdf')}
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}',
               'X-File-Parse': 'True'}
    response = requests.post(url, headers=headers, files=files).json()
    return response


def add_candidate_at_vacancy(candidate_id: int, vacancy_id: int, status_id: int, file_id: int, cv: Dict[str, Any], AUTH_TOKEN):
    url = f"https://dev-100-api.huntflow.dev/account/2/applicants/{candidate_id}/vacancy"
    headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
    data = {
        "vacancy": vacancy_id,
        "status": status_id,
        "comment": cv.get("comment"),
        "files": {
            "id": file_id["id"]
        }
    }
    if status_id == 10:
        data["rejection_reason"] = 1
    response = requests.post(url, headers=headers, json=data)
    return response.json()


# data = parsing_base()
#
# for candidate in data:
#     file_info = upload_file(candidate)
#     candidate_id = add_candidate(candidate, file_info)
#     vacancy_id = get_vacancies_ids(candidate)
#     status_id = get_statuses_ids(candidate)
#     add_candidate_at_vacancy(candidate_id, vacancy_id, status_id, file_info, candidate)
