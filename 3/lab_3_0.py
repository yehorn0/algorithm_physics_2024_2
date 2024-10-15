def reverse_list_in_place(lst):
    left = 0  # Початковий індекс
    right = len(lst) - 1  # Кінцевий індекс

    # Поки індекси не перетнулись
    while left < right:
        # Міняємо місцями елементи
        lst[left], lst[right] = lst[right], lst[left]
        # Зсуваємо індекси
        left += 1
        right -= 1

# Приклад використання
my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print(my_list)  # Виведе: [5, 4, 3, 2, 1]
