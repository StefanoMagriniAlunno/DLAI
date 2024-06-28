# Description: This is an example of a Python module with some functions.

from typing import Union


def hello_world() -> str:
    """Return a string with the message "Hello, World!".

    Returns
    ---
        str: The message "Hello, World!".
    """
    return "Hello, World!"


def test_library(a: int, b: int) -> Union[int, None]:
    """Sum two numbers and return the result.

    Params:
    ---
        - a (int): The first number.
        - b (int): The second number.

    Returns:
    ---
        int: The sum of the two numbers.
        None: If an error occurs.

    Raises:
    ---
        - Exception: If the library is not found.
        - Exception: If the function "sum" is not found in the library.
        - TypeError: If the parameters are not integers.

    Usage:
    ---
        >>> test_library(1, 2)
        3
    """
    # chiamo la funzione "sum" descritta in ./libs/example.so
    from ctypes import cdll

    # uso try per gestire l'eccezione in caso di errore
    try:
        lib = cdll.LoadLibrary("./libs/example.so")
    except Exception as e:
        print("Error:", e)
        return None

    # gestisco l'eccezione se sum non è in lib
    if not hasattr(lib, "sum"):
        raise Exception("Function 'sum' not found in library")

    # calcolo la somma, gestisco l'eccezione se a o b non sono interi
    try:
        res = lib.sum(a, b)
    except TypeError as e:
        print("Error:", e)
        return None

    return res


def hide_func():
    return "This function is hidden"
