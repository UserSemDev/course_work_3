import os
from config import TEST_JSON_PATH
from utils.func import (load_json_file, get_filter_json_file, get_convert_check, get_convert_date,
                        get_info_transaction)


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


def test_get_info_transaction():
    data1 = {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407",
             "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Открытие вклада",
             "to": "Счет 72082042523231456215"}
    data2 = {"id": 716496732, "state": "EXECUTED", "date": "2018-04-04T17:33:34.701093",
             "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации",
             "from": "Visa Gold 5999414228426353", "to": "Счет 72731966109147704472"}
    data3 = {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации",
             "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"}
    data4 = {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
             "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод с карты на карту",
             "from": "Visa Classic 6831982476737658", "to": "Visa Platinum 8990922113665229"}
    assert get_info_transaction(data1) == ("11.07.2018 Открытие вклада\n"
                                           "Аноним -> Счет **6215\n"
                                           "79931.03 руб.")
    assert get_info_transaction(data2) == ("04.04.2018 Перевод организации\n"
                                           "Visa Gold 5999 41** **** 6353 -> Счет **4472\n"
                                           "40701.91 USD")
    assert get_info_transaction(data3) == ("30.06.2018 Перевод организации\n"
                                           "Счет **6952 -> Счет **6702\n"
                                           "9824.07 USD")
    assert get_info_transaction(data4) == ("19.08.2018 Перевод с карты на карту\n"
                                           "Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229\n"
                                           "56883.54 USD")
