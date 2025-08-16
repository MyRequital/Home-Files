"""
Что нужно сделать
Пользователь вводит два числа: N и K.

Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.

"""


def flip_number(num_1, num_2):
    num_1_str = str(num_1)
    num_2_str = str(num_2)

    reversed_num_1 = num_1_str[::-1]
    reversed_num_2 = num_2_str[::-1]

    return reversed_num_1, reversed_num_2


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

reverse_num_1, reverse_num_2 = flip_number(num_1, num_2)

print(f"Первое число наоборот: {reverse_num_1}")
print(f"Второе число наоборот: {reverse_num_2}")