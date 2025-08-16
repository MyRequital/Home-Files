number = int(input("Введите число: "))
for line in range(number):
    for left_number in range(number, number - line - 1, -1):
        print(left_number, end = "")
    point_count = 2 * (number - line - 1)
    print("." * point_count, end = '')
    for right_number in range(number - line, number + 1):
        print(right_number, end = '')
    print()