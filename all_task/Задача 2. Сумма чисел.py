seed_number = int(input("Введите начальное число: "))
end_number = int(input("Введите конечное число: "))
summ_number = 0
for number in range(seed_number, end_number + 1):
    summ_number += number
print("Cумма чисел от ", seed_number, "до", end_number, "равна", summ_number)