import os

from openpyxl import load_workbook

from parse_base import find_base


def write_status_in_excel(code: int, folder_path: str, counter: int):
    if code == 200:
        base_path = find_base(folder_path)
        wb = load_workbook(base_path)
        sheet = wb['Лист1']
        sheet.cell(row=1, column=6, value="Статус")
        sheet.cell(row=counter, column=6, value="Загружено в Хантфлоу")
        os.chdir(folder_path)
        wb.save("Тестовая база.xlsx")
