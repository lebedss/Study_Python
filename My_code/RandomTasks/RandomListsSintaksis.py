# Генерация списка случайных чисел в Python

# Используя random.randint(), мы можем добавлять случайные числа в список.

import random

rand_list = []
n = 10
for i in range(n):
    rand_list.append(random.randint(3, 9))
print(rand_list)

# Метод 2: использование random.sample()

import random

res = random.sample(range(1, 50), 7)

print("Random number list is : " + str(res))

# Метод 3: использование понимания списка + randrange()

import random

res = [random.randrange(1, 50, 1) for i in range(7)]

print("Random number list is : " + str(res))

# Метод 4: использование цикла + randint()

import random
lis = []
for _ in range(10):
    lis.append(random.randint(0, 51))
print(lis)

# Метод 5:Генерация списка случайных целых чисел с использованием функции numpy.random.randint

import numpy as np

# print the list of 10 integers from 3  to 7
print(list(np.random.randint(low=3, high=8, size=10)))

# print the list of 5 integers from 0 to 2
# if high parameter is not passed during
# function call then results are from [0, low)
print(list(np.random.randint(low=3, size=5)))

# Метод 6 Генерация списка случайных плавающих значений с использованием функции numpy.random.random_sample

import numpy as np

# generates list of 4 float values
print(np.random.random_sample(size=4))

# generates 2d list of 4*4
print(np.random.random_sample(size=(4, 4)))