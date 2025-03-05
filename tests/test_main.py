from unittest.mock import patch

import pytest
from main import filter_by_currency


@pytest.mark.parametrize(
    "operations_list, currency, expected_result",
    [
        (
            [
                {
                    "id": 441945886,
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                }
            ],
            "RUB",
            [
                {
                    "id": 441945886,
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                }
            ],
        ),
        (
            [],
            "RUB",
            [],
        ),
    ],
)
def test_search_by_category(operations_list: list[dict], currency: str, expected_result: list[dict]) -> None:
    """Тест проверяет корректный вывод операций по выбранному курсу"""
    assert filter_by_currency(operations_list, currency) == expected_result
