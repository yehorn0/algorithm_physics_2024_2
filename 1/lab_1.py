# Введіть вартість рахунку і відсоток чайових
price = float(input("Введіть вартість рахунку ($xx.xx): "))
tip_percentage = float(input("Введіть відсоток чайових (yy%): "))

# Обчислимо суму чайових
tip_amount = price * (tip_percentage / 100)

# Виведемо результат
print(f"Чайові складають: ${tip_amount:.2f}")
