import math


def myDistance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)


def betweenDistance(x_1, y_1, x_2, y_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(distance)


choice = int(input('1 - расстояние до точки; 2 - расстояние между двумя точками: '))


if choice == 1:
    x = float(input('Введите координату икс: '))
    y = float(input('Введите координату игрек: '))
    myDistance(x, y)
elif choice == 2:
    x_1 = float(input('Введите координату икс первой точки: '))
    y_1 = float(input('Введите координату игрек первой точки: '))
    x_2 = float(input('Введите координату икс второй точки: '))
    y_2 = float(input('Введите координату игрек второй точки: '))
    betweenDistance(x_1, y_1, x_2, y_2)
else:
    print('Ошибка ввода.')
