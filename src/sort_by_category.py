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
