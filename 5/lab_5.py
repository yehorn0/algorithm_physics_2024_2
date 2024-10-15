import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Додавання
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Віднімання
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # Множення
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    # Ділення
    def __truediv__(self, other):
        denominator = other.real  2 + other.imag  2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    # Модуль числа
    def __abs__(self):
        return math.sqrt(self.real  2 + self.imag  2)

    # Перевірка на рівність
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    # Перевірка на нерівність
    def __ne__(self, other):
        return not self.__eq__(other)

    # Переоприділення виведення
    def __str__(self):
        if self.imag < 0:
            return f"{self.real} - {-self.imag}i"
        else:
            return f"{self.real} + {self.imag}i"

    # Інкрементні операції (за бажанням)
    def __isub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __imul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        self.real = real_part
        self.imag = imag_part
        return self

    def __itruediv__(self, other):
        denominator = other.real  2 + other.imag  2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        self.real = real_part
        self.imag = imag_part
        return self

# Приклад використання
a = Complex(3, 2)
b = Complex(1, 7)

print(f"Додавання: {a} + {b} = {a + b}")
print(f"Віднімання: {a} - {b} = {a - b}")
print(f"Множення: {a} * {b} = {a * b}")
print(f"Ділення: {a} / {b} = {a / b}")
print(f"Модуль числа a: |{a}| = {abs(a)}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

# Інкрементні операції
a -= b
print(f"a після a -= b: {a}")
