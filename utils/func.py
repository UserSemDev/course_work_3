import os
import json


def load_json_file(json_file):
    if os.path.exists(json_file):
        with open(json_file) as file:
            data = json.load(file)
        return data
    else:
        return "Файл json не найден"
