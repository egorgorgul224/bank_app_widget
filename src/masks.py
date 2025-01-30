def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX"""

    # if not isinstance(card_number, str):
    #     raise TypeError("Ошибка типа данных")

    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Вы ввели неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает замаскированный номер банковского счета в формате **XXXX, где X - последние 4 цифры счета"""

    # if not isinstance(card_number, str):
    #     raise TypeError("Ошибка типа данных")

    if account_number.isdigit() and len(account_number) == 20:
        return "**" + account_number[-4:]
    else:
        return "Вы ввели неверный номер счета"
