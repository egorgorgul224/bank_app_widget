import csv


def csv_file_reader(path_file: str) -> list[dict]:
    """Функция принимает на вход путь к файлу CSV и возвращает список словарей с транзакциями."""

    csv_operations = []

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            next(reader)
            for operation in reader:
                operation_data = {
                    "id": operation["id"],
                    "state": operation["state"],
                    "date": operation["date"],
                    "operationAmount": {
                        "amount": operation["amount"],
                        "currency": {
                            "currency_name": operation["currency_name"],
                            "currency_code": operation["currency_code"],
                        },
                    },
                    "from_whom": operation["from"],
                    "to_whom": operation["to"],
                    "description": operation["description"],
                }
                csv_operations.append(operation_data)
    except FileNotFoundError:
        print(f"Файл {path_file} не найден")
        return csv_operations

    return csv_operations


if __name__ == "__main__":
    print(csv_file_reader("transactions.csv"))
