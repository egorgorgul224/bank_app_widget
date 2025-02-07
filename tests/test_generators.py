from typing import Generator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# @pytest.mark.parametrize(
#     "currency, expected_result",
#     [
#         (
#             "USD",
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702",
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188",
#             }
#         ),
#     ],
# )
def test_filter_by_currency(transactions_list: list[dict]) -> None:
    result = filter_by_currency(transactions_list, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_wo_transactions(transactions_list: list[dict]) -> None:
    result = filter_by_currency([], "EUR")

    with pytest.raises(StopIteration):
        next(result)


def test_filter_wo_currency(transactions_list: list[dict]) -> None:
    result = filter_by_currency(transactions_list, "")

    with pytest.raises(StopIteration):
        next(result)
