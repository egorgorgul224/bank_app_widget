import pytest

from src.sort_by_category import search_by_category


@pytest.mark.parametrize(
    "operations_list, descriptions_category, expected_result",
    [
        (
            [{"id": 441945800, "description": "Перевод организации"}],
            ["Перевод организации", "Открытие вклада"],
            {"Перевод организации": 1},
        ),
        (
            [],
            ["Перевод организации", "Открытие вклада"],
            {},
        ),
    ],
)
def test_search_by_category(operations_list: list[dict], descriptions_category: list, expected_result: dict) -> None:
    """Тест проверяет корректный возврат словаря, в котором ключи — это названия категорий, а значения — это
    количество операций в каждой категории"""
    assert search_by_category(operations_list, descriptions_category) == expected_result
