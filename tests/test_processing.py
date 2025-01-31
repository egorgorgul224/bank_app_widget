from pickle import FALSE
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
    """Тест проверяет корректное возвращение списка словарей по переданному значению ключа state по умолчанию"""
    assert filter_by_state(dict_list, state) == expected_result


def test_filter_by_state_empty() -> None:
    """Тест проверяет корректное возвращение списка словарей, если список словарей не передан"""
    assert filter_by_state([{}]) == []


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
    ],
)
def test_sort_by_date_default(dict_list: list[dict], expected_result: list[dict], sorting: bool = True) -> None:
    """Тест проверяет возврат верно отсортированного списка словарей по убыванию даты"""
    assert sort_by_date(dict_list, sorting) == expected_result


@pytest.mark.parametrize(
    "sorting, expected_result",
    [
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_date(dict_list: list[dict], expected_result: list[dict], sorting: bool) -> None:
    """Тест проверяет возврат верно отсортированного списка словарей по возрастанию даты"""
    assert sort_by_date(dict_list, sorting) == expected_result


@pytest.mark.parametrize(
    "sorting, expected_result",
    [
        (
            False,
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            True,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
    ],
)
def test_sort_by_same_date(dict_list_with_same_date: list[dict], expected_result: list[dict], sorting: bool) -> None:
    """Тест проверяет вывод верно отсортированного списка словарей с одинаковыми датами по id"""
    assert sort_by_date(dict_list_with_same_date, sorting) == expected_result
