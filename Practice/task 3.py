row_width = int(input("Введите ширину: "))
col_height = int(input("Введите высоту: "))
for row in range(row_width):
    for col in range(col_height):
        if col == 0 or col == col_height - 1:
            print("|", end = "")
        elif row == 0:
            print("-", end = "")
        elif row == row_width -1:
            print("-", end = "")
        else:
            print(" ", end = "")
    print()