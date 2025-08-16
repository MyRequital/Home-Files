sum_num = int(input("Введите кол-во чисел: "))
counter_digit = 0
counter_max = 0
counter_sum = 0
for i in range(sum_num):
    number = int(input("Введите число: "))
    number_copy = number
    counter_digit = 0

    while number > 0:
        counter_digit += number % 10
        number = number // 10

    print(counter_digit)

    if counter_digit > counter_max:
        counter_max = counter_digit
        counter_sum = number_copy

print("число", counter_sum, "имеет максимальную сумму цифр: ", counter_max)