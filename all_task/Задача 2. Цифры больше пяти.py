seq_num = int(input("Кол-во числе в последовательности: "))
num_count = 0
for i in range(seq_num):
    print("Введите", i, "число: ", end = "")
    number = int(input())
    if number > 5:
        num_count += 1
print("Кол-во чисел в последовательности: ", num_count)