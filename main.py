from utils.func import load_json_file, get_filter_json_file, get_select_info_transaction
from config import JSON_PATH


def start():
    data_json = load_json_file(JSON_PATH)
    if isinstance(data_json, list):
        filter_json = get_filter_json_file(data_json)
        while True:
            user_state = input("Какие транзакции вы хотите посмотреть [ВЫПОЛНЕНА(1)/ОТМЕНЕНА(2)]\n"
                               "Введите число 1 или 2: ")
            if user_state.isdigit():
                if int(user_state) in [1, 2]:
                    user_state = int(user_state)
                    break
                else:
                    print("[Error] Неверное число\n")
            else:
                print("[Error] Необходимо ввести число\n")
        print(get_select_info_transaction(filter_json, user_state=user_state))
    else:
        print(data_json)


if __name__ == '__main__':
    start()
