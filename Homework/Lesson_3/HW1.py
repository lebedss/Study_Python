# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая найдёт сумму элементов списка,
#    стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample


def list_rand_nums(count: int):
    if count < 0:
        print("Количество произвольных чисел в списке не может быть отрицательным!")
        return []
    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums


all_list = list_rand_nums(int(input("Введите количество произвольных чисел в списке: ")))
print(f'Наш список, состоящий из произвольных чисел: {all_list}')
print(f'Сумма элементов списка,cтоящих на нечётных позициях - {sum_odd_pos(all_list)}')
