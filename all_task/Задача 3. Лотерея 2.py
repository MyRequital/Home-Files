winners = 0
for ticket in 345, 19, 555, 1020, 421:
    if 99 < ticket < 1000 and ticket % 5 == 0:
        print (ticket, "- Выигрышный билет!")
        winners += 1
print("Кол-во победителей: ", winners)