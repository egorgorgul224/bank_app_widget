import re


def find_data_request(operations: list[dict], user_request: str = "") -> list[dict]:
    """Функция принимает на вход список словарей с данными о банковских операциях и строку поиска. Возвращает
    список словарей, у которых в описании есть данная строка."""

    request_list = []

    format_user_request = user_request.lower().capitalize()

    if operations and user_request:
        for operation in operations:
            pattern = re.compile(rf"{format_user_request}")
            matches = pattern.findall(str(operation.get("description")))
            if matches:
                request_list.append(operation)

    return request_list
