from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция обрабатывает данные о карте или счете и маскирует номер"""
    mask_info = ""
    for account_data in user_data.split():
        if account_data.isdigit() and len(account_data) == 16:
            return f"{mask_info}{get_mask_card_number(account_data)}"
        elif account_data.isdigit() and len(account_data) == 20:
            return f"{mask_info}{get_mask_account(account_data)}"
        else:
            mask_info += account_data + " "
    return "Вы ввели неверный номер банковского счета"
