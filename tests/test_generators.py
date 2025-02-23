import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency,",
    ("USD",),
)
def test_filter_by_currency(transactions_list: list[dict], currency: str) -> None:
    """Тест проверяет корректный вывод операций по выбранному курсу"""
    result = filter_by_currency(transactions_list, currency)
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
    """Тест проверяет, что при передаче пустого списка транзакций обрабатывается ошибка StopIteration"""
    result = filter_by_currency([], "USD")

    with pytest.raises(StopIteration):
        next(result)


def test_filter_wo_currency(transactions_list: list[dict]) -> None:
    """Тест проверяет, что при передаче некорректного курса обрабатывается ошибка StopIteration"""
    result = filter_by_currency(transactions_list, "")

    with pytest.raises(StopIteration):
        next(result)


def test_transaction_descriptions(transactions_list: list[dict]) -> None:
    """Тест проверяет корректный вывод описания каждой транзакции"""
    result = transaction_descriptions(transactions_list)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_empty(transactions_list: list[dict]) -> None:
    """Тест проверяет, что при передаче пустого списка транзакций обрабатывается ошибка StopIteration"""
    result = transaction_descriptions([])

    with pytest.raises(StopIteration):
        next(result)


@pytest.mark.parametrize(
    "start, stop",
    [(9, 11)],
)
def test_card_number_generator(start: int, stop: int) -> None:
    """Тест проверяет корректный вывод номеров карт в заданном диапазоне"""
    result = card_number_generator(start, stop)
    assert next(result) == "0000 0000 0000 0009"
    assert next(result) == "0000 0000 0000 0010"
    assert next(result) == "0000 0000 0000 0011"


@pytest.mark.parametrize(
    "start, stop",
    [(0, 1)],
)
def test_card_number_generator_over_range(start: int, stop: int) -> None:
    """Тест выводит сообщение об ошибке при вводе значения не в диапазоне от 1 до 9999 9999 9999 9999 или
    начального значения, превышающего конечное"""
    result = card_number_generator(start, stop)
    assert next(result) == "Вы ввели некореткный диапозон"
