from typing import Union

from src.file_reader import csv_file_reader, excel_file_reader
from src.processing import filter_by_state, sort_by_date
from src.search_by_request import find_data_request
from src.utils import get_transactions_list
from src.widget import get_date, mask_account_card


def main() -> Union[list[dict], str]:
    """Функция отвечает за основную логику проекта и связывает написанные функциональности между собой."""

    file_format_list = ["JSON-файл", "CSV-файл", "XLSX-файл"]
    operations_status_format = []
    description_list = []

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")

    while True:
        user_file_choice = input(
            """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
        )

        if user_file_choice in ["1", "2", "3"]:
            print(f"Для обработки выбран {file_format_list[int(user_file_choice)-1]}\n")
            if user_file_choice == "1":
                operations_list = get_transactions_list("data/operations")
                break
            elif user_file_choice == "2":
                operations_list = csv_file_reader("transactions.csv")
                break
            else:
                operations_list = excel_file_reader("transactions_excel.xlsx")
                break
        else:
            print("Выберите пункт 1-3 из меню")

    for operation_desc in operations_list:
        if operation_desc.get("description") not in description_list:
            description_list.append(operation_desc.get("description"))
        if operation_desc.get("state") not in operations_status_format:
            operations_status_format.append(operation_desc.get("state"))

    while True:
        user_status_choice = input(
            f"""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: {operations_status_format[:-1]}\n"""
        )

        if user_status_choice.upper() in operations_status_format:
            print(f"Операции отфильтрованы по статусу '{user_status_choice.upper()}'\n")
            filter_operations = filter_by_state(operations_list, user_status_choice.upper())
            break
        else:
            print(f"Статус операции {user_status_choice.upper()} недоступен")

    while True:
        user_filter_data_choice = input("""Отсортировать операции по дате? Да/Нет\n""")

        if user_filter_data_choice.lower() == "да":
            user_filter_data_sort_choice = input("""Отсортировать по возрастанию или по убыванию?\n""")
            if user_filter_data_sort_choice.lower() == "по возрастанию":
                sorted_operations = sort_by_date(filter_operations, False)
                break
            elif user_filter_data_sort_choice.lower() == "по убыванию":
                sorted_operations = sort_by_date(filter_operations)
                break
            else:
                print("Необходимо выбрать: по возрастанию/по убыванию")
        elif user_filter_data_choice.lower() == "нет":
            sorted_operations = filter_operations
            break
        else:
            print("Выберите: Да/Нет")

    while True:
        user_currency_choice = input("""Выводить только рублевые тразакции? Да/Нет\n""")
        if user_currency_choice.lower() == "да":
            sorted_cur_operations = filter_by_currency(sorted_operations, "RUB")
            break
        elif user_currency_choice.lower() == "нет":
            sorted_cur_operations = sorted_operations

            break
        else:
            print("Выберите: Да/Нет")

    while True:
        user_search_choice = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n""")

        if user_search_choice.lower() == "да":
            user_request_choice = input(
                f"""Введите слово или фразу целиком.
Доступные фразы: {description_list[:-1]}\n"""
            )
            search_operations = find_data_request(sorted_cur_operations, user_request_choice.lower().capitalize())
            if search_operations:
                break
            else:
                print("Введено неккоректное слово или фраза")
        elif user_search_choice.lower() == "нет":
            search_operations = sorted_cur_operations
            break
        else:
            print("Выберите: Да/Нет")

    print("Распечатываю итоговый список транзакций...\n")

    print(f"Всего банковских операций в выборке: {len(search_operations)}\n")

    if search_operations:
        total_str = ""
        for operation in search_operations:
            operation_d_m_y = get_date(str(operation.get("date")))
            operation_desc = operation.get("description")
            operation_mask_from = mask_account_card(str(operation.get("from")))
            operation_mask_to = mask_account_card(str(operation.get("to")))
            if user_file_choice == "1":
                operation_amount = operation.get("operationAmount", {}).get("amount", {})
                operation_currency = operation.get("operationAmount", {}).get("currency", {}).get("code", {})
            else:
                operation_amount = operation.get("amount")
                operation_currency = operation.get("currency_code")
            if operation_desc == "Открытие вклада":
                operation_info = f"""{operation_d_m_y} {operation_desc}
{operation_mask_to}
Сумма: {operation_amount} {operation_currency}\n"""
            else:
                operation_info = f"""{operation_d_m_y} {operation_desc}
{operation_mask_from} -> {operation_mask_to}
Сумма: {operation_amount} {operation_currency}\n"""
            total_str += operation_info + "\n"
        return total_str
    else:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"


def filter_by_currency(transactions_list: list[dict], currency: str) -> list[dict]:
    """Функция принимает список транзакций и возвращает генератор с транзакциями по указанному курсу валют"""

    total_list = []
    for transaction in transactions_list:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
            or transaction.get("currency_code") == currency
        ):
            total_list.append(transaction)

    return total_list


if __name__ == "__main__":
    print(main())
