"""
Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N
и находит сумму всех чисел от 1 до N включительно.
Функция вызывается два раза: сначала от числа N, а затем от полученной суммы
"""


def summa_n(n):
    max_num = 0
    for i in range(1, n + 1):
        print(f"{max_num} + {i}", end=" ")
        max_num += i
        print(f"равно {max_num}")
    return max_num


number = int(input("Введите число: "))

new_number = summa_n(number)

new_number = summa_n(new_number)

# ======альтернатива в 1 строку==========
# print(f"{summa_n(summa_n(int(input('Введите число: '))))}")

print(f"двойная сумма от числа {number} = {new_number}")
