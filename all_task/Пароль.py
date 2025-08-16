lock = "abc"
while True:
    unlock = input("Введите пароль: ")
    if unlock == lock:
        print("Вы ввели правильный пароль!")
        break
    else:
        print("Пароль неправильный!")