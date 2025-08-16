dep = int(input("Введите вашу ставку: "))
coef = float(input("Введите кеф: "))

win = round(dep * coef, 2)

print("Общая сумма выигрыша : ", win)
print("Ваша ставка: ", dep, "Чистый выигрыш: ", win - dep)
