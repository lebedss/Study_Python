# Найти индексы максимального и минимального элемента массива - подход через цикл for and if
a = [1, 2, 3, 4, 5]
maximum = a[0]
minimum = a[0]
IndexMax = 0
IndexMin = 0
for i in range(len(a)):
    if a[i] > maximum:
        maximum = a[i]
        IndexMax = i
    if a[i] < minimum:
        minimum = a[i]
        IndexMin = i
print(
    f'элемент с значением: {minimum} минимальный в массиве и его индекс: {IndexMin}')
print(
    f'элемент c значением: {maximum} максимальный в массиве и его индекс: {IndexMax}')

# Найти индексы максимального и минимального элемента массива  - подход через while and if
a = [1, 2, 3, 4, 5]
maximum = a[0]
minimum = a[0]
IndexMax = 0
IndexMin = 0
j = 0
while j < len(a):
    if a[i] > maximum:
        maximum = a[i]
        IndexMax = i
    j += 1
    if a[i] < minimum:
        minimum = a[i]
        IndexMin = i
    j += 1
print(
    f'элемент с значением: {minimum} минимальный в массиве и его индекс: {IndexMin}')
print(
    f'элемент c значением: {maximum} максимальный в массиве и его индекс: {IndexMax}')
