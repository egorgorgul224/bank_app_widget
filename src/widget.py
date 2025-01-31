from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция обрабатывает данные о карте или счете и маскирует номер"""
    user_data_list = user_data.split()

    if user_data == "":
        return "Вы ввели невереный номер карты или счет"

    if user_data_list[0] == "Счет":
        mask_info = get_mask_account(user_data_list[-1])
    else:
        mask_info = get_mask_card_number(user_data_list[-1])

    if mask_info.replace(" ", "").isalpha():
        return mask_info
    else:
        return f"{" ".join(user_data_list[:-1])} {mask_info}"


def get_date(current_date: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    datetime_current_date = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S.%f")
    format_current_date = datetime_current_date.strftime("%d.%m.%Y")
    return format_current_date
