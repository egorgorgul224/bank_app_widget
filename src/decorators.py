from typing import Any, Callable


def int_sum(func):
    """Декоратор возвращает лог с названием функции, результатом, если функция отрабатывает корректно.
    Если функция отрабатывает некорректно, то лог возвращает название функции, ошибку и входные данные."""

    def wrapper(*args):
        try:
            result = func(*args)
            return f"{func.__name__} ok. Result: {result}\n"
        except ZeroDivisionError as zero_log:
            return f"{func.__name__} error: {zero_log}. Inputs: {args}.\n"
        except FileNotFoundError as file_log:
            return f"{func.__name__} error: {file_log}. Inputs: {args}.\n"
        except TypeError as type_log:
            return f"{func.__name__} error: {type_log}. Inputs: {args}.\n"
        except Exception as exc_log:
            return f"{func.__name__} error: {exc_log}. Inputs: {args}.\n"

    return wrapper


def log(filename=None):
    """Декоратор принимает лог с результатом функции и записывает его в лог-файл, если лог-файл указан в параметре.
    Если лог-файл не указан, то возвращает лог в консоль."""

    def decorator(func):
        def wrapper(*args):
            total_message = func(*args)
            if filename:
                with open("mylog.txt", "a", encoding="utf-8") as file:
                    file.write(f"{total_message}")
            else:
                print(f"{total_message}")

        return wrapper

    return decorator


@log(filename="mylog.txt")
@int_sum
def my_function(x, y):
    return x + y


my_function(1, 2)
