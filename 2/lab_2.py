def find_balance_point(weights):
    total_weight = sum(weights)  # Загальна вага
    left_sum = 0  # Сума ваг ліворуч від точки
    
    for i in range(len(weights)):
        right_sum = total_weight - left_sum - weights[i]  # Сума ваг праворуч
        
        # Якщо суми ліворуч і праворуч рівні, це точка опори
        if left_sum == right_sum:
            return i
        
        left_sum += weights[i]  # Додаємо вагу поточного елемента до суми ліворуч
    
    # Якщо не знайшли точку опори
    return -1

# Приклад використання
weights = [1, 3, 5, 9, 2]
balance_point = find_balance_point(weights)
print(f"Точка опори знаходиться на індексі: {balance_point}")


