favorites = 0
for i in range(0,10):
    answer = input("Введи слово,салага!: ")
    if answer == "Карамба" or answer == "карамба":
        print("Тебя бы я взял в далёкое плавание!")
        favorites += 1
    else:
        print("Ты не достойный пират!")
print("Кол-во достойных пиратов: ", favorites)
