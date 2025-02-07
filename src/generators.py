from typing import Any, Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict]:
    """Функция принимает список транзакций и возвращает итератор с транзакциями по указанному курсу"""

    # if filter_dict_list_by_currency == [{}]:
    #     return [{}]

    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Generator[Any]:
    """Функция принимает список транзакций и возвращает описание операций по очереди"""

    for transaction in transactions_list:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Функция принимает начальное и конечное значение карты и генерирует список карт с номерами в диапазоне
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""

    for number in range(start, stop + 1):
        number_generator = "%016d" % number
        yield f"{number_generator[0:4]} {number_generator[4:8]} {number_generator[8:12]} {number_generator[-4:]}"
