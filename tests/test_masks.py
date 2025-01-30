import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_result",
    [("7000792289606361", "7000 79** **** 6361"), ("7000552289601274", "7000 55** **** 1274")],
)
def test_get_mask_card_number(card_number: str, expected_result: str) -> None:
    """Тест проверяет корректную маскировку карты"""
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("", "Вы ввели неверный номер карты"),
        ("700055228960127443", "Вы ввели неверный номер карты"),
        ("as55228960127443", "Вы ввели неверный номер карты"),
    ],
)
def test_get_mask_card_number_error(card_number: str, expected_result: str) -> None:
    """Тест на вывод сообщения об ошибке, если номер карты не 16 символов"""
    assert get_mask_card_number(card_number) == expected_result


# @pytest.mark.parametrize(
#     "card_number",
#     [(7000792289606361), ["7000792289606361", "7000635589606361"]],
# )
# def test_get_mask_card_number_wrong_type(card_number):
#     """Тест на невереный тип входных данных"""
#     with pytest.raises(TypeError):
#         get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number, expected_result",
    [("73654108430135874305", "**4305"), ("73654108430135095651", "**5651")],
)
def test_get_mask_account(account_number: str, expected_result: str) -> None:
    """Тест проверяет корректную маскировку счета"""
    assert get_mask_account(account_number) == expected_result


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        ("", "Вы ввели неверный номер счета"),
        ("700055228960127443", "Вы ввели неверный номер счета"),
        ("as55228960127443", "Вы ввели неверный номер счета"),
    ],
)
def test_get_mask_account_error(account_number: str, expected_result: str) -> None:
    """Тест на вывод сообщения об ошибке, если номер счета не 20 символов"""
    assert get_mask_account(account_number) == expected_result


# @pytest.mark.parametrize(
#     "card_number",
#     [(7000792289606361), ["7000792289606361", "7000635589606361"]],
# )
# def test_gget_mask_account_wrong_type(account_number):
#     """Тест на невереный тип входных данных"""
#     with pytest.raises(TypeError):
#         get_mask_account(account_number)
