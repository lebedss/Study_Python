# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import choices


def list_rand_words(count: int, alp: str = 'xyz'):
    words_list = []
    for i in range(count):
        letters = choices(alp, k=3)
        words_list.append("".join(letters))
    return words_list


def find_sec(word: str, list_words: list):
    if list_words.count(word) > 1:
        index_w = list_words.index(word)
        print(f'Индекс второго вхождения данной строки в списке - {list_words.index(word, index_w + 1)}')
    else:
        print("Второго вхождения данной строки в списке нет")


all_list = list_rand_words(int(input("Введите количество слов: ")))
print(all_list)
find_sec(input("Введите слово из полученного списка: "), all_list)

# Пример и пояснение для функции choices:

# seq = [1, 2, 3, 4, 5, 6]
# random_elements = choices(seq, weights=[20, 1.1, 1, 2.1, 10, 1], k=4)
# print(random_elements)
# Выводит в консоль [5, 1, 1, 5]

# С помощью функции choices(seq [, weights, cum_weights, k]) можно выбрать 1 или несколько элементов из набора данных.
# weights, cum_weights и k — необязательные параметры.
# weights — список относительных весов;
# cum_weights — список кумулятивных (совокупных) весов,
# например weights [10, 5, 30, 5] эквивалентен cum_weights [10, 15, 45, 50].
# k-длина возвращаемого списка(она может быть больше длины переданной последовательности и элементы могут дублироваться)
