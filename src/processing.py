from typing import Optional


def filter_by_state(dict_list: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей по переданному значению ключа state"""
    new_dict_list = []
    for procedure in dict_list:
        if procedure["state"] == state:
            new_dict_list.append(procedure)
    return new_dict_list
