number_debtors = int(input("Введите кол-во должников: "))
debtors_total = 0
for i in range(0, number_debtors + 1, 5):
    print("Должник с номером: ", i)
    debtors_sum = int(input("Сколько должны: "))
    debtors_total += debtors_sum
print("Общая сумма долга: ", debtors_total)