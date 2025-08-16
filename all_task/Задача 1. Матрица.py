n = int(input("Введите число: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 == 0:
            print(i, end='\t')
        else:
            print(j, end='\t')
    print()
