count_numbers = 3

max_number = 0
max_sum_number_digit = 0

for _ in range(count_numbers):
    current_number = int(input("Введите число: "))
    current_number_copy = current_number
    current_sum_digit = 0

    while current_number > 0:
        current_sum_digit += current_number % 10
        current_number //= 10

    if max_sum_number_digit < current_sum_digit:
        max_sum_number_digit = current_sum_digit
        max_number = current_number_copy

print(f"Максимальная сумма чисел у числа {max_number} равна {max_sum_number_digit} ")
