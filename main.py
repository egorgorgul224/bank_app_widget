from src.masks import get_mask_account, get_mask_card_number

card_number = input("Введите номер карты: ")
if card_number.isdigit() and len(card_number) == 16:
    print(get_mask_card_number(card_number))
else:
    print("Вы ввели неверный номер карты")

account_number = input("Введите номер банковского счета: ")
if account_number.isdigit() and len(account_number) == 20:
    print(get_mask_account(account_number))
else:
    print("Вы ввели неверный номер банковского счета")
