"""
У правительства одной из стран есть бухгалтерская программа, которая суммирует налоги её граждан,
компаний плюс НДС с товаров. Страна развивалась, суммарные налоги увеличивались, и бухгалтеры заметили,
что после добавления к общей сумме налогов некого НДС от какого-то продукта общая сумма перестала меняться…

Нужно помочь бухгалтерам: напишите функцию,
на вход которой подаются два числа — общая сумма налога tax и новый налог new_tax, который нужно
добавить к общей сумме. Функция должна проверять, изменится ли показатель степени e при сложении двух чисел.
"""


# def calculate_tax():
#     # tax = input("Введите бюджет страны: ")
#     tax = str("1.2e-12")
#     # new_tax = input("Новые поступления (налог): ")
#     new_tax = str("1.2e1")
#     mantissa_tax, order_tax = tax.split("e")
#     mantissa_new_tax, order_new_tax = new_tax.split("e")
#     mantissa_tax = float(mantissa_tax)
#     order_tax = float(order_tax)
#     mantissa_new_tax = float(mantissa_new_tax)
#     order_new_tax = float(order_tax)
#     mantissa_tax += mantissa_new_tax
#     order_tax += order_new_tax
#     mantissa_tax = str(mantissa_tax)
#     order_tax = str(order_tax)
#     result = float(mantissa_tax) + float(order_tax)
#     # print(result, type(result))
#     # print(tax, type(tax))
#     if float(result) > float(tax):
#         print("Бюджет увеличится")
#     else:
#         print("Бюджет не изменится")

import math


def calculate_tax():
    tax = input("Введите бюджет страны: ")

    new_tax = input("Новые поступления (налог): ")

    mantisa_tax, order_tax = tax.split("e")
    print(f"Мантиса tax = {mantisa_tax}")
    print(f"Ордер tax = {order_tax}")

    mantisa_new_tax, order_new_tax = new_tax.split("e")
    print(f"New_mantisa tax = {mantisa_new_tax}")
    print(f"new_order tax = {order_new_tax}")

    mantisa_tax = float(mantisa_tax) + float(mantisa_new_tax)
    print(f"После сложения mantisa_tax и mantisa_new_tax = {mantisa_tax}")

    order_tax = float(order_tax) + float(order_new_tax)
    print(f"После сложения order_tax и order_new_tax = {order_tax}")

    print(f"\nновые значения мантиса = {mantisa_tax}, новые значения ордер {order_tax}")

    result = float(tax) + float(new_tax)

    order_result = int(math.floor(math.log10(result)))

    print(f"тип tax = {type(tax)}")
    print(f"tax во float = {float(tax)}")

    if order_result > float(tax):
        print("Сумма увеличилась")
    else:
        print("Ничего не изменилось")


calculate_tax()


# import math
#
# def calculate_tax():
#     tax = "1.23e12"
#     new_tax = "1.2e1"
#
#     mantisa_tax, order_tax = tax.split("e")
#     mantisa_new_tax, order_new_tax = new_tax.split("e")
#
#     mantisa_tax = float(mantisa_tax)
#     order_tax = int(order_tax)
#     mantisa_new_tax = float(mantisa_new_tax)
#     order_new_tax = int(order_new_tax)
#
#     tax_value = mantisa_tax * (10 ** order_tax)
#     new_tax_value = mantisa_new_tax * (10 ** order_new_tax)
#
#     total_tax = tax_value + new_tax_value
#
#     print(f"Общий бюджет: {total_tax}")
#
#     # Сравнение с учетом погрешности
#     tolerance = 1e-9  # небольшая погрешность для сравнения чисел с плавающей запятой
#     if math.isclose(total_tax, float(tax), rel_tol=tolerance):
#         print("Бюджет не изменился")
#     elif total_tax > float(tax):
#         print("Бюджет увеличился")
#     else:
#         print("Бюджет уменьшился")
#
#
# calculate_tax()

