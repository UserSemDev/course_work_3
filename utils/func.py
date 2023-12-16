import os
import json
from datetime import datetime


def load_json_file(json_file):
    if os.path.exists(json_file):
        with open(json_file) as file:
            data = json.load(file)
        return data
    else:
        return "Файл json не найден"


def get_filter_json_file(data):
    sorted_data = sorted([i for i in data if i], key=lambda x: x.get('date'), reverse=True)
    return sorted_data


def get_convert_check(data):
    data = data.split(' ')
    finish_check = ""
    if len(data[-1]) == 16:
        check = data[-1][:6] + "*" * 6 + data[-1][-4:]
        finish_check = f"{' '.join(data[:-1])} {' '.join([check[i:i + 4] for i in range(0, 16, 4)])}"
    elif data[0].lower() == 'счет':
        finish_check = f"{' '.join(data[:-1])} **{data[-1][-4:]}"
    return finish_check


def get_convert_date(data):
    date_transaction = datetime.fromisoformat(data.get('date')).strftime('%d.%m.%Y')
    return date_transaction
