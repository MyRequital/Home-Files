height_pyramid = int(input("Введите высоту пирамиды: "))

spaces = height_pyramid - 1
count_symbol = 1

for col in range(height_pyramid):
    print(" " * spaces, "#" * count_symbol)
    count_symbol += 2
    spaces -= 1

