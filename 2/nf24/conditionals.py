# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

#
# if x == y: #if x < y or x > y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")

# if x is y:
#     print(id(x), id(y))
#     print("x IS y")
#
# score = int(input("Enter your score: "))
#
# if 90 <= score:
#     print("A")
# elif 80 <= score:
#     print("B")
# elif 70 <= score:
#     print("C")
# elif 60 <= score:
#     print("D")
# else:
#     print("F")


# def cond_func_simple(ret_val: bool) -> bool:
#     print(f"Ret val: {ret_val}")
#     return ret_val
#
# print(all([True, False, True]))   # False
# print(all([True, True]))          # True
# print(any([True, False, True]))   # True
# print(any([False, False, False])) # False
# if any(
#         [cond_func_simple(True), unknown_function(False), cond_func_simple(True)]
# ):
#     print("Yes")

# if cond_func_simple(True) or unknown_function(False) or cond_func_simple(True):
#     print("Yes")
#
# if cond_func_simple(False) and unknown_function(False) and cond_func_simple(True):
#     print("Yes")
# else:
#     print("No")

# def main():
#     x = int(input("Enter x: "))
#
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
#
#
# def is_even(x: int) -> bool:
#     return x % 2 == 0

    # Ternary
    # return cond ? ret_val1 : ret_val2;  === C
    # return ret_val1 if cond else ret_val2 === python
    #return True if x % 2 == 0 else False

    # simplest
    # if x % 2 == 0:
    #     return True
    # else:
    #     return False


"""
switch (number):
    case 1:
        print("Even")
        break
    ...
    
    default:
...
"""
#from ops.even import is_even
import ops.even as even


def main():
    name = input("")

    if name == "Apple":
        print("Fruit")
    elif name == "Potato":
        print("Veggie")
    elif name == "Strawberry":
        print("Fruit")
    elif name == "Melon":
        print("Fruit")
    elif name == "Watermelon":
        print("What???")

    match name:
        case "Apple" | "Strawberry" | "Melon":
            print("Fruit")
        case "Potato":
            print("Veggie")
        case _:
            print("What???")

    fruit_list = ["Apple", "Melon"]

    if name in fruit_list:
        print("Fruit")


print(__name__)
if __name__ == '__main__':
    print(even.is_even(2), even.__name__)
    #main()
    print("In name main condition")
