# 2. Напишите программу, которая принимает на вход число N 
#    и выдает набор произведений чисел от 1 до N в виде списка.
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]

num = int(input('Введите случайное целое число N: '))
multiplication_result = 1
mylist = []
for i in range(1, num + 1):
    multiplication_result = i * multiplication_result
    mylist.append(multiplication_result)
print(f'Набор произведений чисел от 1 до N в виде списка : {mylist}')
