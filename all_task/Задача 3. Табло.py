number = int(input("Введите число: "))
print("-=-", end=" ")
for i in range(0, number  + 1, 10):
    print(i, end = " -=- ")