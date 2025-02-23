from typing import Any, Callable, Union


def log(filename: str = "") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор возвращает лог с названием функции и результатом, если функция отрабатывает корректно.
    Если функция отрабатывает некорректно, то лог возвращает название функции, ошибку и входные данные.
    Лог отправляется в текстовый файл, если файл передан в параметр, иначе выводит лог в консоль."""

    def sum_args(func: Callable[..., Any]) -> Callable[..., Any]:

        def wrapper(*args: Any) -> Any:
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
def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x / y


my_function(1, 2)
