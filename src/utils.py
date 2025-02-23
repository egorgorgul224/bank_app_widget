import json


def get_transactions_list(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        with open(f"{path_to_file}.json", "r", encoding="utf_8") as transactions_file:
            try:
                transactions_list = json.load(transactions_file)
                if type(transactions_list) == list:
                    return transactions_list
                else:
                    return []
            except json.JSONDecodeError:
                print(f"Ошибка декодирования файла {path_to_file}.json")
                return []
    except FileNotFoundError:
        print(f"Файл {path_to_file}.json не найден")
        return []
