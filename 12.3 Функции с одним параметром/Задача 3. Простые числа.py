"""
Пользователь вводит число N — количество чисел в последовательности.
Напишите функцию  is_prime, которая проверяет, является ли число простым и выводит ответ в консоль.
"""


def is_prime(num):
    for i in range(2, num // 2 + 1):
        print(f"{i}, {num}, {num % i} ")
        if num % i == 0:
            print("Число непростое!")
            break
    else:
        print("Число простое!")


count_num = int(input("Введите кол-во чисел в последовательности: "))

for _ in range(count_num):
    num = int(input("Введите число: "))
    is_prime(num)
