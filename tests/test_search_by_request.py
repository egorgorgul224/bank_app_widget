import pytest

from src.search_by_request import find_data_request


@pytest.mark.parametrize(
    "operations_list, user_request, expected_result",
    [
        (
            [{"id": 441945800, "description": "Перевод организации"}],
            "Перевод",
            [{"id": 441945800, "description": "Перевод организации"}],
        ),
        (
            [{"id": 441945800, "description": "Перевод организации"}],
            "перевод",
            [{"id": 441945800, "description": "Перевод организации"}],
        ),
        (
            [{"id": 441945801, "description": "Перевод организации"}],
            "перевод организации",
            [{"id": 441945801, "description": "Перевод организации"}],
        ),
        (
            [{"id": 441945802, "description": "Перевод организации"}],
            "пЕреВоД ОрганиЗАЦии",
            [{"id": 441945802, "description": "Перевод организации"}],
        ),
        (
            [{"id": 441945810, "description": "Перевод организации"}],
            "Открытие",
            [],
        ),
        (
            [{"id": 441945811, "description": "Перевод организации"}],
            "",
            [],
        ),
        (
            [],
            "Перевод",
            [],
        ),
        (
            [],
            "",
            [],
        ),
    ],
)
def test_find_data_request(operations_list: list[dict], user_request: str, expected_result: list[dict]) -> None:
    """Тест проверяет корректный возврат списка транзакций по строке поиска"""
    assert find_data_request(operations_list, user_request) == expected_result
