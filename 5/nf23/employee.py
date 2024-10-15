class EmployeeSlots:
    __slots__ = ('__name', '__age')

    def __init__(self, name, age):
        print("__init__")
        self.__name = name
        self.__age = age

    def __del__(self):
        print("__del__")


class Employee:
    static_attr = 42
    def __init__(self, name, age):
        print("__init__")
        self.__name = name
        self.__age = age

    def __del__(self):
        print("__del__")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name.capitalize()

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if age < 0:
            raise ValueError("Age must be greater than or equal to zero.")

        self.__age = age

    @name.deleter
    def name(self) -> None:
        # del self.__name
        self.__name = None

    def speak(self) -> None:
        print(f"{self.__name} is {self.age} years old.")

    @staticmethod
    def static_method():
        print(Employee.static_attr)


#employee = ["John", 22, "Manager", 10000]
#employee[1] = -25

def main():
    employee = Employee("John", 25)
    try:
        employee.age = -22
    except ValueError:
        print("Age validation failed.")
    # print(employee.name, employee.age)
    employee.speak()
    Employee.speak(employee)

if __name__ == '__main__':
    main()
