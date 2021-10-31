from openpyxl import load_workbook


def parsing_base():
    wb = load_workbook('D:\Dev\HuntFlow\Тестовая база.xlsx')
    sheet = wb['Лист1']
    cv_list = []
    for cellObj in sheet['A2':'E5']:
        str_from_table = []
        for cell in cellObj:
            str_from_table.append(cell.value)
        cv_dct = {}
        cv_dct['position'] = str_from_table[0]
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
        cv_dct['comments'] = str_from_table[3]
        cv_dct['status'] = str_from_table[4]
        cv_list.append(cv_dct)
    return cv_list
