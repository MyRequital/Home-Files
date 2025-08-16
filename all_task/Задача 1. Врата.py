y_width = int(input("Введите ширину: "))
x_height = int(input("Введите высоту: "))
for y in range(y_width):
    for x in range(x_height):
        if y == 0:
            print("-", end = "")
        elif x == 0 or x == x_height - 1:
            print("|", end = "")
        else:
            print(" ", end = "")

    print()