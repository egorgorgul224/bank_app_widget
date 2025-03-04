import json
from unittest.mock import mock_open, patch

from src.utils import get_transactions_list


def test_get_transactions_list() -> None:
    """Тест проверяет корректный возврат списка словарей с данными о финансовых транзакциях из файла json"""

    mock_data = [{"id": 1, "amount": 100}]
    mock_json_data = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = get_transactions_list("fake_path.json")
        assert result == [{"id": 1, "amount": 100}]


def test_get_transactions_empty_file() -> None:
    """Тест проверяет корректный возврат списка словарей с данными о финансовых транзакциях из пустого файла json"""

    mock_data: list = []
    mock_json_data = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = get_transactions_list("fake_path.json")
        assert result == []


def test_get_transactions_list_arg_not_list() -> None:
    """Тест проверяет корректный вывод из файла json, если в файле содержатся данные, отличные от списка"""

    mock_data = {"id": 1, "amount": 100}
    mock_json_data = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = get_transactions_list("fake_path.json")
        assert result == []


@patch("builtins.open", new_callable=mock_open)
@patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_get_transactions_list_json_error(mock_json_load, mock_open) -> None:
    """Тест проверяет корректную обработку ошибки JSONDecodeError"""

    result = get_transactions_list("fake_path")
    assert result == []  # Ожидаем, что функция вернёт пустой список
    mock_open.assert_called_once_with("fake_path.json", "r", encoding="utf_8")
    mock_json_load.assert_called_once()


@patch("builtins.open", new_callable=mock_open)
@patch("json.load", side_effect=FileNotFoundError("Expecting value", "", 0))
def test_get_transactions_list_file_not_found_error(mock_json_load, mock_open) -> None:
    """Тест проверяет корректную обработку ошибки FileNotFoundError, когда файл не найден"""

    result = get_transactions_list("fake_path")
    assert result == []  # Ожидаем, что функция вернёт пустой список
    mock_open.assert_called_once_with("fake_path.json", "r", encoding="utf_8")
    mock_json_load.assert_called_once()
