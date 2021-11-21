import os
from typing import Any, Dict, List

from openpyxl import load_workbook


def find_resume(path: str, position: str, name: str) -> str:
    """Путь файла с резюме кандидата"""

    folder = os.path.join(path, position)
    for resume in os.listdir(folder):
        if name in resume:
            abs_path = os.path.join(folder, resume)
            return abs_path


def find_base(path: str) -> str:
    """Поиск файла с базой в указанной папке"""
    full_path = os.path.join(path, "Тестовая база.xlsx")
    if os.path.isfile(full_path):
        return full_path


def parsing_base(folder_path: str, verified_data: Dict[str, Any]) -> List:
    """Парсинг Excel и добавление построчно кандидатов в список"""

    base_path = find_base(folder_path)
    wb = load_workbook(base_path)
    sheet = wb[wb.active.title]
    cv_list = []
    for cellObj in sheet[verified_data.get("min_coordinate"):verified_data.get("max_coordinate")]:
        str_from_table = []
        for cell in cellObj:
            str_from_table.append(cell.value)
        cv_dct = {}
        cv_dct['position'] = str_from_table[0]
        cv_dct["full_name"] = str_from_table[1].strip()
        cv_dct["file_path"] = find_resume(folder_path, cv_dct['position'], cv_dct["full_name"])
        split_list = str_from_table[1].strip().split()
        if len(split_list) != 3:
            split_list.insert(2, None)
        cv_dct['last_name'] = split_list[0]
        cv_dct['first_name'] = split_list[1]
        cv_dct['middle_name'] = split_list[2]
        if cv_dct['middle_name'] is None:
            cv_dct.pop('middle_name')
        cv_dct['money'] = str_from_table[2]
        if type(cv_dct['money']) is not str:
            cv_dct['money'] = str(int(cv_dct['money']))
        tmp = cv_dct['money']
        cv_dct['money'] = ''
        for i in tmp:
            if i.isdigit():
                cv_dct['money'] += i
        cv_dct['comment'] = str_from_table[3]
        cv_dct['status'] = str_from_table[4]
        cv_list.append(cv_dct)
    return cv_list
