# 4. * Напишите программу, которая принимает на вход 2 числа.
#      Получите значение N, для пустого списка, заполните числами
#      в диапазоне [-N, N]. Найдите произведение элементов
#      на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

number = int(input("Введите количество элементов [N] для заполнения списка числами в диапазоне [-N, N]: "))
first_position = int(input("Введите любую позицию первого элемента в списке: "))
second_position = int(input("Введите любую позицию второго элемента в списке: "))

numbers_list = list(range(-number, number + 1))
print(f'Список элементов согласно заданным условиям:{numbers_list}')

multiplication_result = numbers_list[first_position - 1] * numbers_list[second_position - 1]
if 0 < first_position and second_position <= len(numbers_list):
    print(f'Произведение элементов на позициях {first_position} и {second_position} = {multiplication_result}')
else:
    print("Для указанных позиций невозможно найти произведение элементов - попробуйте ещё раз")
