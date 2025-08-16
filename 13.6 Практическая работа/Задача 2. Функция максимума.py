


def maximum_of_two(number_1, number_2):
    if number_1 > number_2:
        max_number = number_1
    else:
        max_number = number_2
    return max_number


def maximum_of_three(number_1, number_2, number_3):
    max_number = maximum_of_two(number_1, number_2)
    if max_number < number_3:
        max_number = number_3
    return max_number


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))

max_number = maximum_of_three(number_1, number_2, number_3)

print(max_number)
