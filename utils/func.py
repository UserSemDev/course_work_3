import os
import json
from datetime import datetime


def load_json_file(json_file):
    """Функция загрузки json файла"""
    if os.path.exists(json_file):
        with open(json_file) as file:
            data = json.load(file)
        return data
    else:
        return "Файл json не найден"


def get_filter_json_file(data):
    """Функция сортировки json файла с исключением пустого словаря"""
    sorted_data = sorted([i for i in data if i], key=lambda x: x.get('date'), reverse=True)
    return sorted_data


def get_convert_check(data):
    """Функция формирования номера карты или счета со звездочками"""
    data = data.split(' ')
    finish_check = ""
    if len(data[-1]) == 16:
        check = data[-1][:6] + "*" * 6 + data[-1][-4:]
        finish_check = f"{' '.join(data[:-1])} {' '.join([check[i:i + 4] for i in range(0, 16, 4)])}"
    elif data[0].lower() == 'счет':
        finish_check = f"{' '.join(data[:-1])} **{data[-1][-4:]}"
    return finish_check


def get_convert_date(data):
    """Функция формирования правильного вывода даты"""
    date_transaction = datetime.fromisoformat(data.get('date')).strftime('%d.%m.%Y')
    return date_transaction


def get_info_transaction(data):
    """Функция получения готовой информации о транзакции"""
    date_transact = get_convert_date(data)
    description = data.get('description')
    if data.get('from'):
        check_from = get_convert_check(data.get('from'))
        check_to = get_convert_check(data.get('to'))
        check_from_to = f"{check_from} -> {check_to}"
    else:
        check_to = get_convert_check(data.get('to'))
        check_from_to = f"Аноним -> {check_to}"
    operation_amount = (f"{data['operationAmount']['amount']} "
                        f"{data['operationAmount']['currency']['name']}")
    finish_data = f"{date_transact} {description}\n{check_from_to}\n{operation_amount}"
    return finish_data


def get_select_info_transaction(json_data, user_state):
    """Функция формирующая строку из списка 5 последних транзакций
    1: если выбран EXECUTED
    2: если выбран CANCELED"""
    dict_state = {1: "EXECUTED", 2: "CANCELED"}
    transaction_list = []
    for item in json_data:
        if item.get('state') == dict_state.get(user_state):
            transaction_list.append(get_info_transaction(item))
    return '\n\n'.join(transaction_list[:5])
