def get_number_from_input() -> int:
    return int(input("Enter number: "))

f = get_number_from_input

f.attribute = 5
print(type(f))
print(f.attribute)


