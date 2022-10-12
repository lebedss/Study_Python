# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без использования: встроенной функции преобразования, строк.
# in
# 88
# out
# 1011000

def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(*list_nums, sep="")


conv_bin(int(input()))

# Метод list insert() вставляет элемент в список по указанному индексу.
# Синтаксис метода: list.insert(i, elem)
# Здесь elem вставляется в список по i- му индексу. Все элементы после элемента смещены вправо.

# Префиксные операторы * и **,используются перед переменными в следующих случаях:
# Использование * и ** для передачи аргументов в функцию;
# Использование * и **   для сбора переданных в функцию аргументов;
# Использование ** для принятия только именованных аргументов;
# Использование * при распаковке кортежей;
# Использование * для распаковки итерируемых объектов в список/кортеж;
# Использование ** для распаковки словарей в другие словари.