import os
import tempfile
from typing import Union, Any

from src.decorators import log, my_function


def test_my_function_logs(capsys: Any) -> None:
    """Тест проверяет корректную работу функции my_function"""
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok. Result: 0.5.\n"


def test_my_function_type_error(capsys: Any) -> None:
    """Тест проверяет, что при передаче разных типов данных выводится ошибка unsupported operand type(s)"""
    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (1, '2').\n"


def test_my_function_zero_error(capsys: Any) -> None:
    """Тест проверяет, что при делении на 0 выводится ошибка division by zero"""
    my_function(1, 0)
    captured = capsys.readouterr()
    # assert "my_function error: division by zero. Inputs: (1, 0)." in captured.out
    assert captured.out == "my_function error: division by zero. Inputs: (1, 0).\n"


def test_log_correct() -> None:
    """Тест проверяет корректную работу декоратор log"""

    @log()
    def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x / y

    result = my_function(1, 2)
    assert result == "my_function ok. Result: 0.5."


def test_log_error() -> None:
    """Тест проверяет, что декоратор log выводит ошибку division by zero при делении на 0"""

    @log()
    def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x / y

    result = my_function(1, 0)
    assert result == "my_function error: division by zero. Inputs: (1, 0)."


def test_log_correct_to_file() -> None:
    """Тест проверяет, что декоратор log пердает корректный результат в файл mylog.txt"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
    try:

        @log(filename=temp_filename)
        def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
            return x / y

        my_function(1, 2)

        with open(temp_filename, "r") as file:
            log_content = file.read()
        assert "my_function ok. Result: 0.5.\n" in log_content
    finally:
        os.remove(temp_filename)


def test_log_error_to_file() -> None:
    """Тест проверяет, что декоратор log пердает ошибку division by zero в файл mylog.txt"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
    try:

        @log(filename=temp_filename)
        def my_function(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
            return x / y

        my_function(1, 0)

        with open(temp_filename, "r") as file:
            log_content = file.read()
        assert "my_function error: division by zero. Inputs: (1, 0).\n" in log_content
    finally:
        os.remove(temp_filename)
