list_ = [1, 2, 3, 4, 5, 5, 5, 11, 1, 2, 3, 5, 10, 5, 4]

unique_list_ = []
for x in list_:
    if x not in unique_list_:
        unique_list_.append(x)

print(unique_list_)

unique_set_ = set(list_)
print(unique_set_)

set_1 = {1, 2, 3, 4, 5, 5}
set_2 = {2, 4, 6, 8}

print(set_1 | set_2)
print(set_1.union(set_2))

print(set_1 & set_2)
print(set_1.intersection(set_2))

print(set_1 - set_2) # set_1 - set_1 & set_2
print(set_1.difference(set_2))

print(set_1 ^ set_2) # set_1 | set_2 - set_1 & set_2
print(set_1.symmetric_difference(set_2))

#set_2 = {2, 4, 6, 8}
set_sub_2 = {4, 8}
print(set_sub_2.issubset(set_2))
print(set_2.issuperset(set_sub_2))

set_1.add(3)
print(set_1)
set_1.remove(3)
print(set_1)
