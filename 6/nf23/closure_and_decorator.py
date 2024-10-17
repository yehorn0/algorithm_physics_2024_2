from typing import Callable


def outer_function(msg) -> Callable:
    def inner_function():
        print(msg)

    return inner_function


hello_function = outer_function('Hello')
hello_function()


def decorator_function(original_function: Callable) -> Callable:
    def inner_function(*args, **kwargs):
        print("Inside decorator_function")
        original_function(*args, **kwargs)
        print("After execution")

    return inner_function


@decorator_function
def print_msg_function(msg: str) -> None:
    print(msg)

print_msg_function('Hello')
