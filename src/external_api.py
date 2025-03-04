import os

import requests
from dotenv import load_dotenv


def conversion_to_ruble(from_currency: str, operation_amount: str) -> float:
    """Функция принимает на вход курс валют и сумму в переданной валюте. Возвращает сумму, переведенную в валюту RUB"""

    load_dotenv()
    apilayer_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={operation_amount}"
    payload: dict = {}
    headers = {"apikey": f"{apilayer_key}"}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        return False

    result = response.json()

    return float(result["result"])


def get_transaction_amount(operation_data: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли."""

    if operation_data["operationAmount"]["currency"]["code"] == "RUB":
        amount_data = float(operation_data["operationAmount"]["amount"])

        return amount_data

    else:
        transaction_currency = operation_data["operationAmount"]["currency"]["code"]
        transaction_amount = operation_data["operationAmount"]["amount"]
        conversion_amount = conversion_to_ruble(transaction_currency, transaction_amount)

        return conversion_amount
