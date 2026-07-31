# Запрашиваем значения переменных x и y и приравниваем их к int y пользователя 
x = float(input("What's x? "))
y = float(input("What's y? "))

# Округляем z до целого
z = x / y

print(f"{z:.2f}")