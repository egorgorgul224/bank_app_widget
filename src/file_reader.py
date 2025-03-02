import csv

import pandas as pd


def csv_file_reader(path_file: str) -> list[dict]:
    """Функция принимает на вход путь к файлу CSV и возвращает список словарей с транзакциями."""

    csv_operations = []

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=";")
            for operation in csv_data:
                csv_operations.append(operation)
    except FileNotFoundError:
        print(f"Файл {path_file} не найден")
        return csv_operations

    return csv_operations


def excel_file_reader(path_file: str) -> list[dict]:
    """Функция принимает на вход путь к файлу Excel и возвращает список словарей с транзакциями."""

    excel_operations = []

    try:
        excel_data = pd.read_excel(path_file)
        operations_data = excel_data.to_dict()
        excel_operations.append(operations_data)
    except FileNotFoundError:
        print(f"Файл {path_file} не найден")
        return excel_operations

    return excel_operations


if __name__ == "__main__":
    print(csv_file_reader("transactions.csv"))
    # print(excel_file_reader("transactions_excel.xlsx"))
