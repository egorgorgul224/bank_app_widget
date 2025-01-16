from datetime import datetime

from src.widget import get_date, mask_account_card

card_number = input("Введите номер карты или счета: ")
print(mask_account_card(card_number))

print(get_date(str(datetime.today())))
