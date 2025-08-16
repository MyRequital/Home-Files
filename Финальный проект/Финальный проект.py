# MyProfile app
import sys

separator = '------------------------------------------'

# Переменные для общей информации
name = ''
age = 0
phone = ''
email = ''
additional_information = ''
index = ""
mail = ""
# переменные для информации о предпринимателе
ogrnip = ''
individual_taxpayer_number = ''
current_account = ''
bank_name = ""
bik = ""
correspondent_account = ""


def input_general_info():
    # функция для ввода основной инцофрмации
    global name, age, phone, email, index, mail, additional_information

    name = input('Введите имя: ')
    while True:
        # validate user age
        age = int(input('Введите возраст: '))
        if age > 0:
            break
        print('Возраст должен быть положительным')

    user_phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
    phone = ''
    for character in user_phone_number:
        if character == '+' or ('0' <= character <= '9'):
            phone += character

    email = input('Введите адрес электронной почты: ')
    user_index = input("Введите почтовый индекс: ")
    index = ""
    for symbol in user_index:
        if ("0" <= symbol <= "9"):
            index += symbol

    mail = input("Введите почтовый адрес (без индекса): ")
    additional_information = input('Введите дополнительную информацию:\n')


def input_general_info_entrepreneur():
    # функция для ввода информации о предпринимателе
    global ogrnip, individual_taxpayer_number, current_account, bank_name, bik, correspondent_account
    while True:
        ogrnip = input('Введите ОГРНИП: ')
        if len(ogrnip) != 15:
            print("ОГРНИП должен состоять из 15 цифр!")
        else:
            break
    individual_taxpayer_number = input('Введите ИНН: ')
    while True:
        current_account = input('Введите расчетный счет ')
        if len(current_account) != 20:
            print("Рассчётный счёт должен состоять из 20 цифр!")
        else:
            break
    bank_name = input("Введите название банка: ")
    bik = input("Введите БИК: ")
    correspondent_account = input("Введите Корреспондентский счёт: ")


def general_info_entrepreneur():
    # функция для принта информации о предпринимателе
    print(separator)
    print("Информация о предпринимателе")
    print(f"ОГРНИП: {ogrnip}")
    print(f"ИНН: {individual_taxpayer_number}")
    print("Банковские реквизиты")
    print(f"Расчётный счёт: {current_account}")
    print(f"Название банка: {bank_name}")
    print(f"БИК: {bik}")
    print(f"Корреспондентский счёт: {correspondent_account}")


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, index_parameter, mail_parameter):
    # функция для принта основной информации
    print(separator)
    print('Имя: ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print(f"Индекс: {index}")
    print(f"Почтовый адрес: {mail_parameter}")
    if additional_information:
        print('')
        print('Дополнительная информация:')
        print(index_parameter)


def main_menu():
    # main menu
    print(separator)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        sys.exit()

    if option == 1:
        submenu_1()

    elif option == 2:
        submenu_2()


def submenu_1():
    # submenu 1: Редактировать информацию
    while True:
        print(separator)
        print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
        print('1 - Общая информация')
        print('2 - Информация о предпринимателе')
        print('0 - Назад')

        option_2 = int(input('Введите номер пункта меню: '))
        if option_2 == 0:
            main_menu()
        if option_2 == 1:
            input_general_info()
        elif option_2 == 2:
            input_general_info_entrepreneur()
        else:
            print('Введите корректный пункт меню')


def submenu_2():
    # submenu 2: Принт информации
    while True:
        print(separator)
        print('ВЫВЕСТИ ИНФОРМАЦИЮ')
        print('1 - Общая информация')
        print('2 - Информация о предпринимателе')
        print('3 - Вся информация')
        print('0 - Назад')

        option_2 = int(input('Введите номер пункта меню: '))
        if option_2 == 0:
            main_menu()

        elif option_2 == 1:
            general_info_user(name, age, phone, email, additional_information, mail)

        elif option_2 == 2:
            general_info_entrepreneur()

        elif option_2 == 3:
            general_info_user(name, age, phone, email, additional_information, mail)
            general_info_entrepreneur()

        else:
            print('Введите корректный пункт меню')

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

main_menu()