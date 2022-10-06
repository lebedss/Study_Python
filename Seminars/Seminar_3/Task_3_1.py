# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample


def find_num(count, num):
    if count < 0:
        return "Количество произвольных чисел не может быть отрицательным!"

    list_nums = sample(range(1, count * 2), count)
    print(list_nums)

    if num in list_nums:
        return f"Число - {num} присутствует в заданном списке."
    return f"Число - {num} не присутствует в заданном списке."


print(find_num(int(input("Количество произвольных чисел в списке: ")),
               int(input("Проверить присутствует ли всписке число: "))))

#
# Метод sample(x, y) использует 'x' как массив и 'y' как число значений, которые вам необходимо вернуть.
# Возвращаемая группа не будет содержать дубликатов
#  Но если в исходной последовательности есть неуникальные (повторяющиеся) элементы,
# то каждый их них может появиться в новом списке.
# range - функция создаёт объект range, который представляет собой диапазон чисел.
# Результирующий диапазон чисел включает начальный номер, но исключает конечный (range(0, 10) не включает 10).
