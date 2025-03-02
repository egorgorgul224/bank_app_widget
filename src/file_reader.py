import pandas as pd


def csv_file_reader(path_file: str) -> list[dict]:
    """Функция принимает на вход путь к файлу CSV и возвращает список словарей с транзакциями."""

    try:
        csv_data = pd.read_csv(path_file, delimiter=";")
        operations_data = csv_data.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        print(f"Файл {path_file} не найден")
        return []
    except FileNotFoundError:
        print(f"Файл {path_file} не найден")
        return []

    return operations_data


def excel_file_reader(path_file: str) -> list[dict]:
    """Функция принимает на вход путь к файлу Excel и возвращает список словарей с транзакциями."""

    try:
        excel_data = pd.read_excel(path_file)
        operations_data = excel_data.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Файл {path_file} не найден")
        return []

    return operations_data
