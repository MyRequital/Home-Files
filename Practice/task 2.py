number = int(input("Введите число: "))
row_length = 0 #счётчик длины строки

for i in range(1,number + 1):
    row_length += 1
    for j in range(1,row_length + 1):
        print(i, end = "\t")
    print()
