# def main() -> None:
#     x = get_int()
#
#     print(f"x is {x}")
#
#
def get_int() -> int:
    while True:
        x_str = input("Enter x: ")

        try:
            return int(x_str)
        except ValueError:
            pass
        # except TypeError:
        #     print("Raised TypeError")
        # except NameError | KeyError:
        #     pass
        #else:
            # break
            # return x
        # finally:
        #     print("End cast to int")

    # return x
#
#
# if __name__ == '__main__':
#     main()

# TypeError
# x_int = 1
# y_str = "123"
# print(x_int + y_str)
#
# f_float = 12333.1222
#
# for f in f_float:
#     print(f)

# z_list = [1, 2, 3, 4, 5]
# # z_list[start:end:step]
# print(z_list[:3], z_list[0:3:1]) # z_list[0:3:1]

#
# idx = get_int()
# # if 0 < idx < len(int_list) or -1 >= idx >= -len(int_list):
# #     print(int_list[idx])
# # else:
# #     print("Invalid index")
# try:
#     print(int_list[idx])
# except IndexError:
#     print("Invalid index")

# int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # -> [[1,2,3], [4,5,6], [7,8,9], [10]]
#
#
# def chunk_list(lst: list[int], chunk_length: int) -> list[list[int]]:
#     chunked_list = []
#     # count = len(lst) // chunk_length
#     #
#     # if len(lst) % chunk_length != 0:
#     #     count += 1
#     #
#     # for chunk_number in range(count):
#     #     chunked_list.append(
#     #         lst[chunk_number * chunk_length:(chunk_number + 1) * chunk_length]
#     #     )
#     chunk_number = 0
#     while True:
#         chunk = lst[chunk_number * chunk_length:(chunk_number + 1) * chunk_length]
#         if chunk:
#             chunked_list.append(chunk)
#
#         if len(chunk) < chunk_length:
#             break
#
#         chunk_number += 1
#
#     return chunked_list
#
# print(chunk_list(int_list, 3))

# KeyError
# things_dict = {
#     "apple": "fruit",
#     "melon": "fruit",
#     "strawberry": "fruit",
#     "potato": "vegetable"
# }
#
# try:
#     type_ = things_dict["none"]
# except KeyError:
#     print("KeyError")
#     type_ = "fruit_default"
#
# if "none" in things_dict:
#     type_ = things_dict["none"]
# else:
#     type_ = "fruit_default"
#
# print(things_dict.get("none", "fruit_default"))
#
# print(type_)
#
# a_int = 1222
#
# attr_value = getattr(
#     a_int,
#     "attr",
#     "attr_value"
# )
# print(attr_value)

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # -> [[1,2,3], [4,5,6], [7,8,9], [10]]

reversed_list = []

try:
    while elem := int_list.pop():
        reversed_list.append(elem)
except IndexError:
    pass

print(reversed_list, int_list)

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(reversed(int_list)))


# print(int_list.reverse())

print(int_list[::-1], int_list)