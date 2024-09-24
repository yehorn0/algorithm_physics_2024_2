# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
#
# print(f"{round(x+y):.2f}")
#
# print(f"{x/y}")
#
# print(f"{x/y:.3f}")
from typing import Callable


def clear_input_capitalize(s: str) -> str:
    return s.strip().capitalize()


def clear_input_title(s: str) -> str:
    return s.strip().title()


#def hello(name: str = "world", clear_func: Callable = clear_input_capitalize) -> None:
def hello(name="world", clear_func=clear_input_capitalize) -> None:
    print(f"hello {clear_func(name)}")

hello()

n = input("Enter your name: ")
hello(name=n, clear_func=clear_input_title)

# hello(int(name))
# duck
# object Duck
# Duck.walk, Duck.squeel -> Duck -> class(duck)
