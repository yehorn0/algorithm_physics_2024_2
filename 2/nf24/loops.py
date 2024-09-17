# count = 3
#
# while count:
#     print(count)
#     count -= 1  # count = count - 1
#
# # count = 0
# while count < 3:
#     print(count)
#     count += 1  # count = count + 1


# for i in range(3): #(0, 1, 2) <=> [0,3)
#     print(i)

#
# for i in range(3, 20, 3): #range(start, end, step)
#     print(i)

fruit_list = ["Apple", "Melon", "Strawberry", "Watermelon"]


print(f"Length: {len(fruit_list)}")

idx = 0
for idx in range(len(fruit_list)):
    print(f"{idx+1}. {fruit_list[idx]}")

print()

for idx, fruit in enumerate(fruit_list):
    print(f"{idx + 1}. {fruit}")

things_dict = {
    "apple": "fruit",
    "melon": "fruit",
    "strawberry": "fruit",
    "potato": "vegetable"
}

print()

for thing in things_dict:
    print(thing, things_dict[thing], sep=": ")
print()

for thing, thing_value in things_dict.items():
    print(thing, thing_value, sep=": ")
