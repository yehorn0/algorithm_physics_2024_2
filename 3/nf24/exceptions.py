# x_str = input("Enter x: ")
#
# try:
#     x = int(x_str)
# except ValueError:
#     print("Invalid input")
# else:
#     print(f"x is {x}")
# finally:
#     print("End type cast to int")

# def main() -> None:
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int() -> int:
#     while True:
#         x_str = input("Enter x: ")
#         try:
#             return int(x_str)
#         except ValueError:
#             pass
#             #print("Invalid input")
#         # else:
#         #     #break
#         #     return x
#         #
#     # return x
#
# if __name__ == '__main__':
#     main()
#
# x_int = 1
# y_str = "123"
# print(x_int + y_str)
# y_str()
#
# z_list = [1, 2, 3, 4, 6]
# print(z_list["1"])
#
# a_float = 135456.2234
#
# for i in a_float:
#     print(i)

# IndexError
# int_list = [1, 2, 3,
#             4, 5, 6,
#             7, 8, 9,
#             10] #10
# # list[start:end:step]
# chunk_len = 3
#
# def chunk_list(lst: list[int], chunk_len: int) -> list[list[int]]:
#     chunked_list = []
#     count = len(lst) // chunk_len + 1
#
#     for i in range(count):
#         # yield lst[i * chunk_len : (i + 1) * chunk_len]
#         chunked_list.append(
#             lst[i * chunk_len:(i + 1) * chunk_len]
#         )
#     # chunk_idx = 0
#     #
#     # while True:
#     #     chunk = lst[chunk_idx * chunk_len:(chunk_idx + 1) * chunk_len]
#     #
#     #     if chunk:
#     #         chunked_list.append(chunk)
#     #
#     #     if len(chunk) < chunk_len:
#     #         break
#     #     chunk_idx += 1
#
#     return chunked_list
#
# # print(chunk_list(int_list, chunk_len))
#
# reversed_list = []
#
# try:
#     while elem := int_list.pop():
#         reversed_list.append(elem)
# except IndexError:
#     pass
#
# print(reversed_list)
# int_list = [1, 2, 3,
#             4, 5, 6,
#             7, 8, 9,
#             10] #10
#
# for x in reversed(int_list):
#     print(x)
#
# int_list.reverse()
# print(int_list)
#
# int_list = [1, 2, 3,
#             4, 5, 6,
#             7, 8, 9,
#             10] #10
# print(int_list[::-1])
# print(int_list[:5:2])
# print(int_list[0:len(int_list):1])  # <=> int_list[::]  <=> int_list[]

# a = [1,2,3,4] => [4,3,2,1]
"""
id | name| grade|....| ...|...|..
1  | V   | A    |
...
..

2000|...
"""

# KeyError
# things_dict = {
#     "apple": "fruit",
#     "melon": "fruit",
#     "strawberry": "fruit",
#     "potato": "vegetable"
# }
# # try:
# #     type_ = things_dict["none"]
# # except KeyError:
# #     type_ = "fruit"
#
# type_ = things_dict.get("none", "fruit")
#
# things_dict.setdefault("none", "fruit")
# things_dict.setdefault("none", "veg")
#
# print(things_dict)

# AttributeError

# a_int = 1
#
# try:
#     print(a_int.attr)
# except AttributeError:
#     print("No attr for int")
#
# #print(a_int.non_existing_method())
#
# attr_value = getattr(
#     a_int,
#     "attr",
#     "attr_default_value"
# )
#
# print(attr_value)
#
# class A:
#     def __init__(self, a):
#         self.attr = a
#
# obj_A = A(1)
#
# # obj_A.non_attr

try:
    raise ExceptionGroup("multiple errors occurred", [ValueError("error 1"), TypeError("error 2")])
except* ValueError as e:
    print("Caught ValueError:", e)
except* TypeError as e:
    print("Caught TypeError:", e)
