number = int(input("Введите число: "))
chair_total = 0
for n in range(1, number + 1, 5):
    print("Номер стула: ", n)
    chair_total += n
print("Сумма: ", chair_total)