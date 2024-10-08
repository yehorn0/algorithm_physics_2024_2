class Employee:
    # __slots__ = ('name', 'age')

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __del__(self):
        print("Destructor called")


def main() -> None:
    employee = Employee("John", 22)
    # employee.salary = 2500

    print(employee.name, employee.age)
    print(employee)
    del employee
    # print(employee)

    employee_list = ["Name", 22, "Manager", 3000]
    employee_dict = {
        "name": "John",
        # ....
    }


if __name__ == '__main__':
    main()
