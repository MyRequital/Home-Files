"""
Пользователь вводит два числа: А и В.
Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B.
Используйте list comprehensions (как и в следующих задачах).
"""

even_numbers = [number for number in range(int(input("Введите от какого числа: ")), int(input("Введите до какого числа: ")) + 1) if number % 2 == 0]
print(even_numbers)