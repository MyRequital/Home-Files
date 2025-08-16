pyramid_height = int(input("Введите высоту пирамиды: "))
new_num = 1
for line in range(pyramid_height):
    space_count = pyramid_height - line -1
    print("   " * space_count, end = "")
    for number in range(line + 1):
        print(new_num, end = "    ")
        new_num += 2
    print()
