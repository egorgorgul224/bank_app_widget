from collections import Counter


def search_by_category(operations: list[dict], descriptions_category: list) -> dict:
    """Функция принимает на вход список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории."""

    result_dict = {}
    description_list = []

    for operation in operations:
        description_list.append(operation.get("description"))

    counted = Counter(description_list)

    for key, values in counted.items():
        for category in descriptions_category:
            if category == key:
                result_dict[category] = values

    return result_dict


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
    description = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
    ]
    print(search_by_category(operations_list, description))
