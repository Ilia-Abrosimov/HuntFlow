from api import (add_candidate, add_candidate_at_vacancy, get_statuses_ids,
                 get_vacancies_ids, upload_file)
from excel_operations import check_status_in_excel, write_status_in_excel
from parse_base import parsing_base


def flow(path: str, token: str) -> str:
    """Основная функция скрипта"""

    checked_data = check_status_in_excel(path)
    if checked_data == "База уже загружена в Хантфлоу":
        return "База уже загружена в Хантфлоу"
    data = parsing_base(path, checked_data)
    counter = checked_data.get("counter")
    for candidate in data:
        file_info = upload_file(candidate, token)
        candidate_id = add_candidate(candidate, file_info, token)
        vacancy_id = get_vacancies_ids(candidate, token)
        status_id = get_statuses_ids(candidate, token)
        status_code = add_candidate_at_vacancy(candidate_id, vacancy_id, status_id, file_info, candidate, token)
        write_status_in_excel(status_code, path, counter)
        counter += 1
    return "Скрипт выполнен"
