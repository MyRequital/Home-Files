getting_started = int(input("Во сколько начался рабочий день? "))
hours_worked = 0
rested_total = 0
for hours in range(getting_started, 20):
    print("сейчас", hours, "часов")
    hours_worked += 1
    rested = int(input("Сколько уделил время отдыху? "))
    rested_total += rested
    if rested_total >= 45:
        print("Цель достигнута можешь продолжать работать с комфортом!")
        break
print("Всего минут активности: ", rested_total)
print("Часов работы: ", hours_worked)