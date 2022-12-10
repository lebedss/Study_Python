# число, факториал которого нужно вычислить
num = int(input())
# начальное значение факториала
factorial = 1

# Если num является натуральным и положительным, то
if num % 1 == 0 and num >= 0:
    # Вычисляем факториал числа num
    for i in range(1, num + 1):
        factorial = i * factorial
    # Выводим результат на экран
    print(f'{num}! = {factorial}')
# Если num - отрицательное или нецелое число, выводим сообщение об ошибке
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')