# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
# # <, >, <=, >=, ==, !=, is, in
# # and, or..
# # if x != y:
# #     print("x is not equal to y")
# # # elif x > y: # heavy_function(x, y)
# # #     print("x is bigger than y")
# # #elif x == y:
# # else:
# #     print("x is equal to y")
#
# # if x == y:
# #     print("x and y are equal")
# # else:
# #     print("x and y are not equal")
#
# if x is y:
#     print("x is y")
# else:
#     print("x is not y")
# print(f"{id(x)}, {id(x)}")
#
# a = [1, 2 ,3]
# b = [1, 2 ,3]
# print(a == b)
# print(a is b)
# print(f"{id(a}, {id(b)}")
#
# score = int(input('Enter your score: '))
#
# if 90 <= score: # if False then score < 90
#     print('A')
# elif 80 <= score:
#     print('B')
# elif 70 <= score:
#     print('C')
# #elif score >= 60 and score <= 70:
# elif 60 <= score:
#     print('D')
# else:
#     print('F')

def main_int_even() -> None:
    x = int(input("Enter x: "))

    if is_even(x): # 5 // 2 = 2
        print("Even")
    else:
        print("Odd")


def is_even(x: int) -> bool:
    # # Zero attempt
    # if x % 2 == 0:  # 5 // 2 = 2
    #     return True
    # else:
    #     return False

    # # First attempt (ternary operator)
    # # C/C++/js...: condition ? ret_val_if_true : ret_val_if_false
    # # python: ret_val_if_true if condition else ret_val_if_false
    # return True if x % 2 == 0 else False

    return x % 2 == 0


def main_match():
    """c/c++/js
    switch (variable):
        case 1:
            ....

        case 2:
            ...
        default:
            ...
    """
    name = input("Enter name: ")
    #if name == "Adam" or name == "Peter" or name == "Simon":
    #    print("NF-12")
    match name:
        case "Adam" | "Peter" | "Simon":
            print("NF-12")
        case "John":
            print("NF-11")
        # case "Peter":
        #     print("NF-12")
        case "Anna":
            print("NF-13")
        # case "Simon":
        #     print("NF-12")
        case _:
            print("Invalid input")


def main_conditions_execution():
    x = int(input("Enter x: "))

    def is_number_not_equal(number: int, condition: int) -> bool:
        print(f"is_number_not_equal: {number} == {condition}")
        return number != condition

    def is_number_equal(number: int, condition: int) -> bool:
        print(f"is_number_equal: {number} == {condition}")
        return number == condition

    # if is_even(x) and is_number_not_equal(x, 2) and is_number_not_equal(x, 4) and is_number_equal___not_defined(x, 6):
    #     print("Even and not equal to two or four")
    # else:
    #     print("Odd")

    # if all([
    #         is_even(x), is_number_not_equal(x, 2), is_number_not_equal(x, 4), is_number_equal___not_defined(x, 6)
    # ]):
    #     print("Even and not equal to two or four")
    # else:
    #     print("Odd")

    if any([is_even(x), is_number_equal(x, 5)]):
        print("Even or 5")
    else:
        print("Odd and not 5")


if __name__ == '__main__':
    main_conditions_execution()
