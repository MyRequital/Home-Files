"""
Вы пришли на работу в компанию по разработке игр,
целевая аудитория — дети и их родители. У предыдущего программиста было задание
сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
Однако программист, на место которого вы пришли, перед увольнением не успел выполнить
эту задачу и оставил только небольшой шаблон проекта.

Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит,
победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он не угадает загаданное.

Что нужно сделать
Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
"""
import random


def rock_paper_scissors():
    # Здесь будет игра «Камень, ножницы, бумага»

    choice_opponent = random.choice(("камень", "ножницы", "бумага"))
    print("Если захотите выйти напишите: выход")
    choice_user = input("Что выбираете? Камень? ножницы? бумага?: ").lower()

    if (choice_user != "камень") and (choice_user != "ножницы") and (choice_user != "бумага"):
        print("Ошибка ввода!")
        rock_paper_scissors()

    print("Соперник сделал выбор...")

    if choice_opponent == "камень":
        if choice_user == "камень":
            print(f"Ничья! соперник выбрал {choice_opponent}")
        elif choice_user == "ножницы":
            print(f"Вы проиграли! соперник выбрал {choice_opponent}")
        elif choice_user == "бумага":
            print(f"Вы выиграли! соперник выбрал {choice_opponent}")

    elif choice_opponent == "бумага":
        if choice_user == "камень":
            print(f"Вы проиграли! соперник выбрал {choice_opponent}")
        elif choice_user == "ножницы":
            print(f"Вы выиграли! соперник выбрал {choice_opponent}")
        elif choice_user == "бумага":
            print(f"Ничья! соперник выбрал {choice_opponent}")

    elif choice_opponent == "ножницы":
        if choice_user == "камень":
            print(f"Вы проиграли! соперник выбрал {choice_opponent}")
        elif choice_user == "ножницы":
            print(f"Ничья! соперник выбрал {choice_opponent}")
        elif choice_user == "бумага":
            print(f"Вы выиграли! соперник выбрал {choice_opponent}")
    elif choice_user == "выход":
        main_menu()
    main_menu()


def guess_the_number():
    # Здесь будет игра «Угадай число»
    random_number = random.randint(1,10)
    print("Магическое число загадано...")
    choise_user = int(input("угадайте число от 1 до 10: "))
    if choise_user == random_number:
        print("Вы угадали! Забирайте джекпот!!!")
    else:
        print(f"Вы проиграли! магическое число было: {random_number}")
    main_menu()


def main_menu():
    # Здесь главное меню игры
    answer = int(input("в какую игру будем играть: "
                       "\n 1 - камень,ножницы,бумага"
                       "\n 2 - угадай число: "))
    if answer == 1:
        rock_paper_scissors()
    elif answer == 2:
        guess_the_number()
    else:
        print("Ошибка ввода!")
        main_menu()


main_menu()