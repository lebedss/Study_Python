# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt

print('Введите координаты точки А: ')
Xa = float(input('x: '))
Ya = float(input('y: '))
print('Введите координаты точки B: ')
Xb = float(input('x: '))
Yb = float(input('y: '))

print(f'Расстояние между точками A и B: {round(sqrt((Xa - Xb) ** 2 + (Ya - Yb) ** 2), 2)}')
