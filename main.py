from datetime import datetime

from src.widget import mask_account_card, get_date

card_number = input("Введите номер карты или счета: ")
print(mask_account_card(card_number))

print(get_date(str(datetime.today())))