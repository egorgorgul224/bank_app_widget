from typing import Any, Callable


def log(filename: str = ""):
    """Декоратор возвращает лог с названием функции и результатом, если функция отрабатывает корректно.
    Если функция отрабатывает некорректно, то лог возвращает название функции, ошибку и входные данные.
    Лог отправляется в текстовый файл, если файл передан в параметр, иначе выводит лог в консоль."""

    def sum_args(func):

        def wrapper(*args):
            try:
                result = func(*args)
                message = f"{func.__name__} ok. Result: {result}."
            except ZeroDivisionError as zero_log:
                message = f"{func.__name__} error: {zero_log}. Inputs: {args}."
            except FileNotFoundError as file_log:
                message = f"{func.__name__} error: {file_log}. Inputs: {args}."
            except TypeError as type_log:
                message = f"{func.__name__} error: {type_log}. Inputs: {args}."
            except Exception as exc_log:
                message = f"{func.__name__} error: {exc_log}. Inputs: {args}."

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{message}\n")
            else:
                print(message)
                return message

        return wrapper

    return sum_args


@log()
def my_function(x, y):
    return x / y


my_function(1, 2)
