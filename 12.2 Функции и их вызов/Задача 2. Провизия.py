"""
Одна государственная компания поставляет еду на разные труднодоступные базы
(полярные, горные и так далее) в разных уголках страны. В компании для удобства
расчёта количества еды была реализована такая программа:
"""

total_products = 0


def sum_products():
    global total_products
    first_product = int(input("Введите кол-во первого продукта: "))
    second_product = int(input("Введите кол-во второго продукта: "))
    print(f"Всего {first_product + second_product} шт\n")
    total_products += first_product + second_product


print("Сколько мешков рыбы и мяса? ")
sum_products()

print("Сколько буханок белого и чёрного хлеба? ")
sum_products()

print("Сколько вёдер воды и молока? ")
sum_products()

print(f"Всего продуктов {total_products} ")