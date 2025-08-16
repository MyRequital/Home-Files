"""
Степан использует калькулятор для расчёта суммы и разности чисел,
но на работе ему требуются не только обычные арифметические действия.
Он ничего не хочет делать вручную, поэтому решил немного расширить функциональность калькулятора.

Что нужно сделать
Напишите программу, запрашивающую у пользователя число и действие,
которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.
Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
"""


def exit():
    print("\nВсего хорошего!")


def examination(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number = number // 10
    print(f"Сумма цифр: {sum_digits}")
    main()


def max_number(number):
    max_num = 0
    while number > 0:
        if number % 10 > max_num:
            max_num = number % 10
        number = number // 10
    print(f"Максимальное число: {max_num}")
    main()


def min_number(number):
    min_num = number
    while number > 0:
        if number % 10 < min_num:
            min_num = number % 10
        number = number // 10
    print(f"Минимальное число: {min_num}")
    main()


def main():
    number = int(input("Введите число: "))
    action_number = int(input("Введите номер действия: "
                              "\n1 - сумма цифр"
                              "\n2 - максимальная цифра"
                              "\n3 - минимальная цифра: "
                              "\n4 - завершить программу: "))
    if action_number == 1:
        examination(number)
    elif action_number == 2:
        max_number(number)
    elif action_number == 3:
        min_number(number)
    elif action_number == 4:
        exit()
    else:
        print("Ошибка ввода!")
        main()


main()


