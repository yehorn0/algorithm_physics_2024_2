def get_name_from_input() -> str:
    def inner_function() -> None:
        print("inner function")

    return input("Enter name: ")

def outer_function() -> None:
    print("outer function")

get_name_from_input.any_attribute = 5
get_name_from_input.function = outer_function

print(get_name_from_input())
print(get_name_from_input.any_attribute)
print(get_name_from_input.function())
