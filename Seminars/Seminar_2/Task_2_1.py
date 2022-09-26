# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# 1-ый вариант
num = int(input())
result = 1
for i in range(num):
    print(result, end=" ")
    result *= -3
print()
# 2-ой вариант
num = int(input())
for i in range(num):
    print(-(3) ** i, end=" ")
