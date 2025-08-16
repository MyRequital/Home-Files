#
#           #Решение через функцию:
# number_1 = int(input("Введите первое число: "))
# number_2 = int(input("Введите второе число: "))
#
#
# def calculating_largest():
#     max_number = 0
#     if number_1 > number_2:
#         max_number = number_1
#     elif number_2 > number_1:
#         max_number = number_2
#     else:
#         max_number = number_1
#
#     for i in range(1, (max_number // 2) + 1):
#         if number_1 % i == 0 and number_2 % i == 0:
#             max_number = i
#     print(f"Максимальный общий делитель: {max_number}")
#
#
# calculating_largest()



#             решение через модуль math
# import math
#
# number_1 = int(input("Введите первое число: "))
# number_2 = int(input("Введите второе число: "))
#
# print(math.gcd(number_1, number_2))


