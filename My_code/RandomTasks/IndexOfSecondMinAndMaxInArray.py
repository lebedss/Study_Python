# Задан массив заполненый числами - необходимо найти второй после max элемент второй после минимума
numbers = [1, 8, 3, 2, 6]
size = len(numbers)
current_index = 0
max_number_index = 0
maximum = numbers[0]
while current_index < size:
    if numbers[current_index] > maximum:
        maximum = numbers[current_index]
        max_number_index = current_index
    current_index += 1
current_index = 0
second_maximum = numbers[0]
if max_number_index == 0:
    second_maximum = numbers[1]
while current_index < size:
    if current_index != max_number_index:
        if numbers[current_index] > second_maximum:
            second_maximum = numbers[current_index]
    current_index += 1
print("Второе максимальное по величене значение элемента массива:", second_maximum)
min_number_index = 0
minimum = numbers[0]
while current_index < size:
    if numbers[current_index] < minimum:
        minimum = numbers[current_index]
        min_number_index = current_index
    current_index += 1
current_index = 0
second_minimum = numbers[0]
if min_number_index == 0:
    second_minimum = numbers[1]
while current_index < size:
    if current_index != min_number_index:
        if numbers[current_index] < second_minimum:
            second_minimum = numbers[current_index]
    current_index += 1
print("Второе минимальное по величене значение элемента массива:", second_minimum)

# Задан массив заполненый числами - необходимо найти второй после max элемент второй после min элемент.
# Завернул условия в цикл
numbers = [1, 8, 3, 2, 6]
size = len(numbers)
current_index = 0
max_number_index = 0
maximum = numbers[0]
min_number_index = 0
minimum = numbers[0]
while current_index < size:
    if numbers[current_index] > maximum:
        maximum = numbers[current_index]
        max_number_index = current_index
    if numbers[current_index] < minimum:
        minimum = numbers[current_index]
        min_number_index = current_index
    current_index += 1
current_index = 0
second_maximum = numbers[0]
second_minimum = numbers[0]
if max_number_index == 0:
    second_maximum = numbers[1]
if min_number_index == 0:
    second_minimum = numbers[1]
while current_index < size:
    if current_index != max_number_index:
        if numbers[current_index] > second_maximum:
            second_maximum = numbers[current_index]
    if current_index != min_number_index:
        if numbers[current_index] < second_minimum:
            second_minimum = numbers[current_index]
    current_index += 1
print(f'Второй маскимум в массиве: {second_maximum} Второй минимум в массиве: {second_minimum}')

# Как более эффективно решить эту задачу?
numbers = [1, 8, 3, 2, 6]
size = len(numbers)
first_maximum = numbers[0]
second_maximum = numbers[0]
first_minimum = numbers[0]
second_minimum = numbers[0]
if numbers[1] > first_maximum:
    first_maximum = numbers[1]
else:
    second_maximum = numbers[1]
if numbers[1] < first_minimum:
    first_minimum = numbers[1]
else:
    second_minimum = numbers[1]
current_index = 2
while current_index < size:
    if numbers[current_index] > first_maximum:
        second_maximum = first_maximum
        first_maximum = numbers[current_index]
    if numbers[current_index] < first_minimum:
        second_minimum = first_minimum
        first_minimum = numbers[current_index]
    else:
        if numbers[current_index] > second_maximum:
            second_maximum = numbers[current_index]
        if numbers[current_index] < second_minimum:
            second_minimum = numbers[current_index]
    current_index += 1
print(f'Второй маскимум в массиве: {second_maximum} Второй минимум в массиве: {second_minimum}')
