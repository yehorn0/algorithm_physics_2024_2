def print_msg_function(msg: str) -> None:
    try:
        print(msg[0])
    except IndexError:
        return
    print_msg_function(msg[1:])


print_msg_function("Hello")

def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(10))