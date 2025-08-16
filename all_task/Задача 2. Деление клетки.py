total_hour = int(input("Введите кол-во часов: "))
cell = 1
for hour in range(1, total_hour //3 + 1):
    cell *= 2
    print("Прошло часов: ", hour *3)
    print("Кол-во клеток: ", cell)
    print("Осталось часов: ", total_hour - hour *3)
    print()
print("Задача выполнена!")