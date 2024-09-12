from typing import Callable


def clean_name(name: str) -> str:
    return name.strip().title()


def clean_name_upper(name: str) -> str:
    return name.strip().upper()


def hello_untyped(name="vasia"):
    print(f"hello {name.upper()}!")


def hello(name: str = "vasia", clean_func: Callable = clean_name) -> None:
    def hello_func():
        print("in the inner func")

    hello_func()
    cleaned_name = clean_func(name)

    print(f"hello {cleaned_name}!")


def main():
    name = clean_name(input("Enter name: "))
    hello_untyped()
    hello(name, clean_func=clean_name_upper)


#main()

if __name__ == "__main__":
    main()
