from typing import Optional


def filter_by_state(dict_list: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по переданному значению ключа state"""
    filter_dict_list = []

    if dict_list == [{}]:
        return [{}]

    for procedure in dict_list:
        if procedure.get("state") == state:
            filter_dict_list.append(procedure)
    return filter_dict_list


def sort_by_date(dict_list: list[dict], sorting: bool = True) -> list[dict]:
    """Функция возвращает новый список словарей, отсортированный по дате(по умолчанию - сортировка по убыванию)"""
    sorted_dict_list = sorted(dict_list, key=lambda date: (date.get("date"), date.get("id")), reverse=sorting)
    return sorted_dict_list
