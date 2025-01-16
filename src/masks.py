def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты в формате XXXX XX** **** XXXX"""

    return f"{card_number[0:4]} {card_number[5:7]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает замаскированный номер банковского счета в формате **XXXX, где X - последние 4 цифры счета"""

    return "**" + account_number[-4:]
