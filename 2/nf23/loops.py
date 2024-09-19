# i = 0
#
# while i < 3:
#     print("in loop")
#
#     i += 1

# forEach
# for counter in range(10, 1, 1):  # [0, 3) ~ 0,1,2
#     print(f"{counter}. In for loop.")

# range(start, end, step)
# range(3) -> range(0, 3, 1)
# range(2, 5, 2) -> 2, 4
# range(10, 1, -3) -> (10, 7, 4)
# range(10, 1, 1) -> ()
# a = [1,2,3,4,5] -> a[start:end:step]

# nf_12_students = ["Adam", "Peter", "Simon"]
# # print(nf_12_students[0])
# # print(nf_12_students[1])
# # print(nf_12_students[2])
# #print(nf_12_students[3]) - raised IndexError
#
# # for idx in range(len(nf_12_students)):
# #     print(f"{idx + 1}. {nf_12_students[idx]}")
#
# for idx, student in enumerate(nf_12_students):
#     print(f"{idx + 1}. {student}")

#
# student_list = ["Adam", "Peter", "Simon", "John", "Anna"]
# deps = ["nf-12", "nf-12", "nf-12", "nf-11", "nf-13"]
#
# students = [
#     {"name": "Adam", "group": "nf-12", "average": 10.},
#     {"name": "Peter", "group": "nf-12", "average": 12.},
#     {"name": "Simon", "group": "nf-12", "average": 14.},
#     {"name": "John", "group": "nf-11", "average": 20.},
#     {"name": "Anna", "group": "nf-13", "average": 30.},
# ]
# # print(students["Adam"])
# # print(students["Adam_not_in_students"]) # KeyError
#
# # for student, group in students.items():
# #     print(f"{student}, Group: {group}")
# for student in students:
#     print(student["name"], student["group"], student["average"], sep=", ")

student_names = "Adam, Peter, Simon, John, Anna" # -> ["Adam", "Peter", "Simon", "John", "Anna"]

def get_student_names(names_string: str) -> list[str]:
    names: list[str] = []
    current_name: str = ""

    names_string = names_string.replace(" ", "")

    for char in names_string:
        if char == ",":
            names.append(current_name)
            current_name = ""
            continue
        current_name += char
    else:
        names.append(current_name)

    return names

student_names_list = student_names.split(", ")
print(get_student_names(student_names))

print(student_names.split(", ", maxsplit=2))

print(student_names.rsplit(", ", maxsplit=2))

print("!@. ".join(student_names_list))
