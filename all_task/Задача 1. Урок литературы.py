bad_rating = 0
for student in range(5):
    answer = input("Кто написал произведение? ")
    if (answer == "Лермонтов") or (answer == "лермонтов"):
        print("Молодец,все правильно!")
        break
    print("Неверно! садись Два!")
    bad_rating += 1
print("Кол-во двоек", bad_rating)
