import os
from config import TEST_JSON_PATH
from utils.func import load_json_file, get_filter_json_file, get_convert_check, get_convert_date


def test_load_json_file():
    path1 = os.path.join(TEST_JSON_PATH, 'has_data_operations.json')
    assert load_json_file(path1) == [{"1": "one"}, {"2": "two"}, {"3": "three"}]
    path2 = os.path.join(TEST_JSON_PATH, 'has_null_operations.json')
    assert load_json_file(path2) == []
    path3 = os.path.join(TEST_JSON_PATH, 'file_not_found.json')
    assert load_json_file(path3) == "Файл json не найден"


def test_get_filter_json_file():
    data = [{"date": "2018-06-30T02:08:58.425572"},
            {"date": "2019-07-03T18:35:29.512364"},
            {"date": "2019-08-26T10:50:58.294041"}]
    assert get_filter_json_file(data) == [{"date": "2019-08-26T10:50:58.294041"},
                                          {"date": "2019-07-03T18:35:29.512364"},
                                          {"date": "2018-06-30T02:08:58.425572"}]


def test_get_convert_check():
    data1 = "Счет 64686473678894779589"
    data2 = "Maestro 1596837868705199"
    data3 = "Visa Platinum 8990922113665229"
    assert get_convert_check(data1) == "Счет **9589"
    assert get_convert_check(data2) == "Maestro 1596 83** **** 5199"
    assert get_convert_check(data3) == "Visa Platinum 8990 92** **** 5229"


def test_get_convert_date():
    date_transaction = {"date": "2018-07-11T02:26:18.671407"}
    assert get_convert_date(date_transaction) == "11.07.2018"
