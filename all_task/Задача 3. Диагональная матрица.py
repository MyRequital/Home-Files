n = int(input("Введите размер матрицы: "))

for y in range(n):
    for x in range(n):
        buf_x = (n - 1) - y  # вспомогательное число, которое будет уменьшаться от n-1 до 0
        if buf_x > x:
            print(0, end='\t')
        elif buf_x == x:
            print(1, end='\t')
        else:
            print(2, end='\t')
    print()