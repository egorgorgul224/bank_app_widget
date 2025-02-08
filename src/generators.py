from typing import Any, Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict]:
    """Функция принимает список транзакций и возвращает итератор с транзакциями по указанному курсу"""

    for transaction in transactions_list:
        try:
            if transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency:
                yield transaction
        except StopIteration:
            continue


def transaction_descriptions(transactions_list: list[dict]) -> Generator[Any]:
    """Функция принимает список транзакций и возвращает описание операций по очереди"""

    for transaction in transactions_list:
        try:
            yield transaction.get("description")
        except StopIteration:
            continue


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Функция принимает начальное и конечное значение карты и генерирует список карт с номерами в диапазоне
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""

    # if start > stop:
    #     start = stop
    #     stop = start + 1
    if start > stop or start < 1 or stop > 9999999999999999:
        yield "Вы ввели некореткный диапозон"

    for number in range(start, stop + 1):
        number_generator = "%016d" % number
        yield f"{number_generator[0:4]} {number_generator[4:8]} {number_generator[8:12]} {number_generator[-4:]}"
