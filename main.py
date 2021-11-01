from api import (add_candidate, add_candidate_at_vacancy, get_statuses_ids,
                 get_vacancies_ids, upload_file)
from parse_base import parsing_base

if __name__ == "__main__":
    path = input("Введите пуль к папке с базой: ")
    token = input("Введите токен: ")
    data = parsing_base(path)
    for candidate in data:
        file_info = upload_file(candidate, token)
        candidate_id = add_candidate(candidate, file_info, token)
        vacancy_id = get_vacancies_ids(candidate, token)
        status_id = get_statuses_ids(candidate, token)
        add_candidate_at_vacancy(candidate_id, vacancy_id, status_id, file_info, candidate, token)
    print("Скрипт выполнен")
