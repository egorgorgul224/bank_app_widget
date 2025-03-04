import re


def find_data_request(operations: list[dict], user_request: str) -> list[dict]:
    """Функция принимает на вход список словарей с данными о банковских операциях и строку поиска. Возвращает
    список словарей, у которых в описании есть данная строка."""

    request_list = []

    for operation in operations:
        color_pattern = re.compile(rf"{user_request.title()}")
        matches = color_pattern.findall(operation.get("description"))
        if matches:
            request_list.append(operation)

    return request_list


if __name__ == "__main__":
    operations_list = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    print(find_data_request(operations_list, "перевод"))
