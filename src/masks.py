import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX"""

    if not isinstance(card_number, str):
        logger.error("Ошибка типа данных: введен некорректный тип данных")
        raise TypeError("Ошибка типа данных")

    logger.info(f"Маскируем номер карты {card_number}")
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Маскировка номера карты выполнена успешно")
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.info("Неверный номер карты: должно быть 16 цифр")
        return "Вы ввели неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает замаскированный номер банковского счета в формате **XXXX, где X - последние 4 цифры счета"""

    if not isinstance(account_number, str):
        logger.error("Ошибка типа данных: введен некорректный тип данных")
        raise TypeError("Ошибка типа данных")

    logger.info(f"Маскируем номер счета {account_number}")
    if account_number.isdigit() and len(account_number) == 20:
        logger.info("Маскировка номера счета выполнена успешно")
        return "**" + account_number[-4:]
    else:
        logger.info("Неверный номер счета: должно быть 20 цифр")
        return "Вы ввели неверный номер счета"
