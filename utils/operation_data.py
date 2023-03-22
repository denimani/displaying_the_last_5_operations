import json


def open_operations_file():
    with open('C:\\Users\\Программист\\PycharmProjects\\Course_work_3\\utils\\operations.json', encoding='utf-8') as f:
        return json.load(f)


def last_five_operations():
    """
    Функция возвращает список последних 5 успешных операций из всего списка операций пользователя.
    :return: список последних 5 успешных операций
    """
    list_executed_operations = []
    count = 0
    for operation in open_operations_file():
        if operation['state'] == 'EXECUTED':
            count += 1
            list_executed_operations.append(operation)
            if count == 5:
                return list_executed_operations
