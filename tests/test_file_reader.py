from unittest.mock import mock_open, patch

import pandas as pd

from src.file_reader import csv_file_reader, excel_file_reader


def test_csv_file_reader() -> None:
    """Тест проверяет корректный возврат списка словарей с транзакциями из указанного csv файла"""

    mock_data = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;"
        "Счет 39745660563456619397;Перевод организации\n"
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = csv_file_reader("fake")
        assert result == [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]


def test_csv_file_reader_empty() -> None:
    """Тест проверяет корректный возврат пустого списка, если файл csv пустой"""

    mock_data = None
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = csv_file_reader("fake")
        assert result == []


@patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_csv_file_reader_not_found_error(mock_read_csv) -> None:
    """Тест проверяет корректный возврат пустого списка, если csv файл не найден"""

    result = csv_file_reader("fake.csv")
    assert result == []


@patch("pandas.read_excel")
def test_excel_file_reader(mock_read_excel) -> None:
    """Тест проверяет корректный возврат списка словарей с транзакциями из указанного excel файла"""

    mock_data = pd.DataFrame({"id": [650703, 3598919], "state": ["EXECUTED", "EXECUTED"]})
    mock_read_excel.return_value = mock_data

    result = excel_file_reader("fake")
    expected = [
        {"id": 650703, "state": "EXECUTED"},
        {"id": 3598919, "state": "EXECUTED"},
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_excel_file_reader_empty(mock_read_excel) -> None:
    """Тест проверяет корректный возврат пустого списка, если файл excel пустой"""

    mock_data = pd.DataFrame()
    mock_read_excel.return_value = mock_data

    result = excel_file_reader("fake")
    assert result == []


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_excel_file_reader_not_found_error(mock_read_excel) -> None:
    """Тест проверяет корректный возврат пустого списка, если excel файл не найден"""

    result = excel_file_reader("fake")
    assert result == []
