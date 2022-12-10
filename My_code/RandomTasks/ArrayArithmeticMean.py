# Задача 2. Напишите псевдокод по блок-схеме
# Нахождение срдеднеарифмитического значения суммы элементов заданного одномерного массива

numbers = [2, 5, 13, 7, 6, 4]
size = 6
ArraySum = 0  # синтаксис языка Python не позволяет взять имя переменной из блок схемы - sum поскольку под данным
# наименованием зарезервированную функцию
index = 0
ArithmeticMean = 0
while index < size:
    ArraySum = ArraySum + numbers[index]
    index += 1
ArithmeticMean = ArraySum / size
print(ArithmeticMean)
