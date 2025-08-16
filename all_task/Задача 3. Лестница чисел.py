number = int(input("Введите число: "))
for i in range(number + 1):
    for j in range(i,number + 1):
        print(j, end="\t")
    print()