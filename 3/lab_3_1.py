import math

# Функція для знаходження НСД (найбільшого спільного дільника) для всіх елементів списку
def find_gcd(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

# Функція для знаходження НСК (найменшого спільного кратного) для всіх елементів списку
def find_lcm(arr):
    lcm = arr[0]
    for num in arr[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm

# Основна функція
def find_numbers(a, b):
    # Знаходимо НСК для всіх елементів списку a
    lcm_a = find_lcm(a)
    
    # Знаходимо НСД для всіх елементів списку b
    gcd_b = find_gcd(b)
    
    # Знаходимо всі числа, які кратні lcm_a і на які ділиться gcd_b
    result = []
    for num in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % num == 0:
            result.append(num)
    
    return result

# Приклад списків
a = [2, 4]
b = [16, 32, 96]

# Виклик функції
result = find_numbers(a, b)
print(result)  # Виведе: [4, 8, 16]
