import json


def open_operations_file():
    with open("operations.json", encoding='utf-8') as f:
        return json.load(f)


def last_five_operations():
    """
    Функция возвращает список последних 5 успешных операций из всего списка операций пользователя.
    :return: список последних 5 успешных операций
    """
    list_executed_operations = []
    count = 0
    for operation in sorted(open_operations_file(), key=lambda x: x['date'], reverse=True):
        if operation['state'] == 'EXECUTED':
            count += 1
            list_executed_operations.append(operation)
            if count == 5:
                return list_executed_operations
