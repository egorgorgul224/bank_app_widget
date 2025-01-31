import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "user_data, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(user_data: str, expected_result: str) -> None:
    """Тест проверяет корректную маскировку карты или счета"""
    assert mask_account_card(user_data) == expected_result


@pytest.mark.parametrize(
    "user_data, expected_result",
    [
        ("", "Вы ввели невереный номер карты или счет"),
        ("Счет 646864736788947", "Вы ввели неверный номер счета"),
        ("MasterCard 71583007", "Вы ввели неверный номер карты"),
        ("Счет 353830334744478955602323", "Вы ввели неверный номер счета"),
        ("Visa Classic 683198247673765834343", "Вы ввели неверный номер карты"),
        ("Visa Platinum", "Вы ввели неверный номер карты"),
        ("Счет", "Вы ввели неверный номер счета"),
    ],
)
def test_mask_account_card_error(user_data: str, expected_result: str) -> None:
    """Тест на вывод сообщения об ошибке, если номер карты не 16 символо или номер счета не 20 символов"""
    assert mask_account_card(user_data) == expected_result


@pytest.mark.parametrize(
    "current_date, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-05-25 02:26:18.671407", "25.05.2022"),
        ("25-05-2024T02:26:18.671407", "25.05.2024"),
        ("25-Jan-2024 02:26:18.671407", "25.01.2024")
    ],
)
def test_get_date(current_date: str, expected_result: str) -> None:
    """Тест на вывод даты в формате ДД.ММ.ГГГГ"""
    assert get_date(current_date) == expected_result


@pytest.mark.parametrize(
    "current_date, expected_result",
    [
        ("", "Введена невереная дата"),
        ("12032024", "Введена невереная дата")

    ],
)
def test_get_date_error(current_date: str, expected_result: str) -> None:
    """Тест на вывод сообщения об ошибке, если передана неверная дата"""
    assert get_date(current_date) == expected_result
