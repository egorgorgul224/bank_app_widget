from datetime import datetime

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
    return "Вы ввели неверный номер карты или банковского счета"


def get_date(current_date: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    datetime_current_date = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S.%f")
    format_current_date = datetime_current_date.strftime("%d.%m.%Y")
    return format_current_date
