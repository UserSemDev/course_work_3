import os
import json


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
