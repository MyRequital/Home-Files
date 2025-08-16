seq_num = int(input("Введите кол-во чисел: "))
quantity_seq_num = 0
for _ in range(seq_num):
    number = int(input("Введите число: "))
    for i in range(2,number // 2 + 1):
        if number % i == 0:
            break
    else:
        quantity_seq_num += 1
        print("Найденое простое число: ", number)
print("Количество простых чисел в последовательности: ", quantity_seq_num)