from utils.func import load_json_file, get_filter_json_file, get_select_info_transaction
from config import JSON_PATH


def start():
    # загружаем json файл
    data_json = load_json_file(JSON_PATH)
    # если данные типа list продолжаем иначе else
    if isinstance(data_json, list):
        # фильтруем загруженный json
        filter_json = get_filter_json_file(data_json)
        while True:
            # получаем от пользователя данные какие транзакции он хочет посмотреть
            user_state = input("Какие транзакции вы хотите посмотреть [ВЫПОЛНЕНА(1)/ОТМЕНЕНА(2)]\n"
                               "Введите число 1 или 2: ")
            # если ответ число идем далее иначе else
            if user_state.isdigit():
                # если ответ 1 или 2 выходим из цикла иначе else
                if int(user_state) in [1, 2]:
                    user_state = int(user_state)
                    break
                else:
                    print("[Error] Неверное число\n")
            else:
                print("[Error] Необходимо ввести число\n")
        # вывод последних 5 операций
        print(get_select_info_transaction(filter_json, user_state=user_state))
    else:
        print(data_json)


if __name__ == '__main__':
    start()
