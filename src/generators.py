from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict]:
    """Функция принимает список транзакций и возвращает итератор с транзакциями по указанному курсу"""

    # if filter_dict_list_by_currency == [{}]:
    #     return [{}]

    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency:
            yield transaction
