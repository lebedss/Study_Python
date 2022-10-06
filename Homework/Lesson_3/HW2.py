# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample


def list_rand_nums(count):
    if count < 0:
        print("Количество произвольных чисел в списке не может быть отрицательным")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def prod_pairs(list_nums: list):
    res_list = []

    for k in range(len(list_nums) // 2):
        res_list.append(list_nums[k] * list_nums[len(list_nums) - k - 1])

    if len(list_nums) % 2:
        res_list.append(list_nums[len(list_nums) // 2])
    return res_list


all_list = list_rand_nums(int(input("Введите количество произвольных чисел в списке: ")))
print(f'Наш список, состоящий из произвольных чисел: {all_list}')
print(f'Произведение пар чисел списка: {prod_pairs(all_list)}')
