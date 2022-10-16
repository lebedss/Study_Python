# Сумма цифр числа
num = int(input("Введите целое: "))
digits_sum = 0
while num > 0:
    digits_sum = digits_sum + num % 10
    num = num // 10
print("Сумма цифр числа равна:", digits_sum)

# Произведение цифр числа
num = int(input("Введите целое: "))
multiplication = 1
while num != 0:
    multiplication = multiplication * (num % 10)
    num = num // 10
print("Произведение цифр равно: ", multiplication)
