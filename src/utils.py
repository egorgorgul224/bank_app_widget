import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_list(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        logger.info(f"Выполняем открытие и чтение файла {path_to_file}.json")
        with open(f"{path_to_file}.json", "r", encoding="utf_8") as transactions_file:
            try:
                logger.info(f"Файл открыт. Выполняем преобразование файла {path_to_file}.json в объект Python")
                transactions_list = json.load(transactions_file)
                if isinstance(transactions_list, list):
                    logger.info(f"Файл {path_to_file}.json успешно преобразован в объект Python")
                    return transactions_list
                else:
                    logger.error("Файл не содержит список")
                    return []
            except json.JSONDecodeError:
                logger.error(f"Ошибка декодирования файла {path_to_file}.json")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {path_to_file}.json не найден")
        return []
