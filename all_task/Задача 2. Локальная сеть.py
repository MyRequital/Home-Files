number = int(input("Введите число: "))
step = int(input("Введите шаг: "))
summ = 0
print("\nIP-адрес:", end = " ")
for count in range(3):
    print(number, end = ".")
    summ += number
    number += step
print(summ)