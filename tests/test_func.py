import os
from config import TEST_JSON_PATH
from utils.func import load_json_file


def test_load_json_file():
    path1 = os.path.join(TEST_JSON_PATH, 'has_data_operations.json')
    assert load_json_file(path1) == [{"1": "one"}, {"2": "two"}, {"3": "three"}]
    path2 = os.path.join(TEST_JSON_PATH, 'has_null_operations.json')
    assert load_json_file(path2) == []
    path3 = os.path.join(TEST_JSON_PATH, 'file_not_found.json')
    assert load_json_file(path3) == "Файл json не найден"
