import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import conversion_to_ruble, get_transaction_amount


@pytest.mark.parametrize(
    "operation_data, expected_result",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "100", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            100,
        ),
    ],
)
def test_get_transaction_amount(operation_data: dict, expected_result: float) -> None:
    """Тест проверяет корректный вывод суммы в рублях, когда транзакция была выполнена в валюте RUB"""

    assert get_transaction_amount(operation_data) == expected_result


@patch("requests.request")
def test_get_transaction_amount_not_rub(mocked_get) -> None:
    """Тест проверяет корректный вывод суммы в рублях, когда транзакция была выполнена не в валюте RUB"""

    load_dotenv()
    apilayer_key = os.getenv("API_KEY")
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 100},
        "info": {"timestamp": 1740212351, "rate": 88.810669},
        "date": "2025-02-22",
        "result": 7900.0222,
    }
    result = get_transaction_amount(
        {
            "id": 441941136,
            "state": "EXECUTED",
            "date": "2017-08-26T10:50:58.294041",
            "operationAmount": {"amount": "100", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
    assert result == 7900.0222
    mocked_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=100",
        headers={"apikey": f"{apilayer_key}"},
        data={},
    )


@patch("requests.request")
def test_conversion_to_ruble(mocked_get):
    """Тест проверяет корректный вывод суммы транзакции, переведенной из валюты(отличной от RUB) в рубли RUB"""

    load_dotenv()
    apilayer_key = os.getenv("API_KEY")
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 100},
        "info": {"timestamp": 1740212351, "rate": 88.810669},
        "date": "2025-02-22",
        "result": 8881.0669,
    }
    result = conversion_to_ruble("USD", "100")
    assert result == 8881.0669
    mocked_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": f"{apilayer_key}"},
        data={},
    )


@patch("requests.request")
def test_get_user_info_invalid(mocked_get):
    """Тест проверяет корректную обработку случая, когда status code запроса не успешен(не равен 200)"""

    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    result = conversion_to_ruble("USD", "100")
    assert result == False
