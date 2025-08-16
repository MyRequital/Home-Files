wake_up = int(input("Во сколько проснулся: "))
water = 0
calories_total = 0
for n in range(wake_up, 23 + 1, 3):
    print("Проснулся в: ", n)
    water += 1
    calories = int(input("Сколько калорий съел: "))
    calories_total += calories
print("Выпил литров воды: ", water)
print("Потреблено калорий: ", calories_total)
