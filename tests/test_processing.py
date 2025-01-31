from typing import Optional

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_result",
    [
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
(
            "RETANINED",
            [],
        ),
    ],
)
def test_filter_by_state(dict_list: list[dict], state: str, expected_result: list[dict]) -> None:
    """Тест проверяет корректное возвращение списка словарей по переданному значению ключа state"""
    assert filter_by_state(dict_list, state) == expected_result


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        ),
    ],
)
def test_filter_by_default_state(
    dict_list: list[dict], expected_result: list[dict], state: Optional[str] = "EXECUTED") -> None:
    """Тест проверяет корректное возвращение списка словарей по переданному по умолчанию значению ключа state"""
    assert filter_by_state(dict_list, state) == expected_result


def test_filter_by_state_empty() -> None:
    """Тест проверяет корректное возвращение списка словарей, если список словарей не передан"""
    assert filter_by_state([{}]) == []
