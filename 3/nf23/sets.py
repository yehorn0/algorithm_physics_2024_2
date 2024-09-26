# list_ = [1, 2, 3, 4, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 5]
#
# unique_list = []
#
# for elem in list_:
#     if elem not in unique_list:
#         unique_list.append(elem)
#
# print(unique_list)
#
# unique_set = set(list_)
#
# print(unique_set)

set_1 = {1, 2, 3, 4, 8, 11, 10}

# set_2 = set()
#
# for number in range(10):
#     if number % 2 == 0:
#         set_2.add(number)
#
# comprehension
# a + b = b + a
set_2 = {number for number in range(1, 10) if number % 2 == 0} # {2,4,6,8}

print(set_1 | set_2)
print(set_1.union(set_2), set_2.union(set_1))

print(set_1 & set_2)
print(set_1.intersection(set_2), set_2.intersection(set_1))

print(set_1 - set_2, set_2 - set_1) # set_1 - set_1 & set_2
print(set_1.difference(set_2), set_2.difference(set_1))

print(set_1 ^ set_2, set_2 ^ set_1) # set_1 | set_2 - set_1 & set_2
print(set_1.symmetric_difference(set_2), set_2.symmetric_difference(set_1))

subset_2 = {2}

print(subset_2.issubset(set_2))
print(subset_2.issuperset(set_2))
print(set_2.issuperset(subset_2))

print(set_1)
set_1.add(3)
print(set_1)
set_1.add(5)
print(set_1)
set_1.remove(3)
print(set_1)
set_1.remove(3)
print(set_1)
