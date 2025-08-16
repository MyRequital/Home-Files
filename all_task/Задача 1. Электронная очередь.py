people = int(input("Введите кол-во людей в очереди: "))
for hour in range(people + 1):
    print("Идет", hour, "час")
    for num in range(hour,people):
        print("Номер в очереди", num)
    print()
print("Очередь обслужена!")