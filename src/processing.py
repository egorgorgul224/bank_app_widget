from typing import Optional


def filter_by_state(dict_list: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по переданному значению ключа state"""
    new_dict_list = []
    for procedure in dict_list:
        if procedure["state"] == state:
            new_dict_list.append(procedure)
    return new_dict_list


def sort_by_date(dict_list: list[dict], sorting: bool = True) -> list[dict]:
    """Функция возвращает новый список словарей, отсортированный по дате(по умолчанию - сортировка по убыванию)"""
    sorted_dict_list = sorted(dict_list, key=lambda date: date.get("date", "1980-01-01"), reverse=sorting)
    return sorted_dict_list
