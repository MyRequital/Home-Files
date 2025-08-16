"""
В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи,
а затем уже идут небольшие. Каждая из этих задач, по сути, просто огромный поток цифр.
Ваша задача, как программиста этого центра, написать программу, которая поможет определять,
какую из задач нужно решать в первую очередь.

Вводится последовательность из N чисел. Нужно определить номер числа, у которого больше всего цифр,
и вывести на экран соответствующее сообщение. Если число отрицательное,
то считать его за 0. Для подсчёта количества цифр реализуйте функцию numeral_count.
"""

def numeral_count(n):
    return int(len(str(n)))


def max_len_num():
    task_quantity = int(input("Введите кол-во задач: "))
    max_len = 0
    max_number = 0

    for i in range(task_quantity):
        number = int(input("Введите число: "))

        if number < 0:
            number = 0
        current_len = numeral_count(number)

        print(current_len)

        if current_len > max_len:
            max_len = current_len
            max_number = number

        print(max_number)

    return max_number


print(f"Первая задача на обработку: {max_len_num()}")