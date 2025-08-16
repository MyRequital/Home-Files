#coordinat_1 = 6
#coordinat_2 = 19
#stop_coordinat_1 = 20
#stop_coordinat_2 = 0
#while True:
#    print("Марсоход находится на позиции:", coordinat_1, coordinat_2, "введите команду:")
#    answer = input(" ")
#    if answer == "a" or answer == "A" and coordinat_1 != stop_coordinat_2 and coordinat_1 != stop_coordinat_1:
#        coordinat_1 -= 1
#    elif answer == "d" or answer == "D" and coordinat_1 != stop_coordinat_2 and coordinat_1 != stop_coordinat_1:
#        coordinat_1 += 1
#    elif answer == "w" or answer == "W" and coordinat_2 != stop_coordinat_2 and coordinat_2 != stop_coordinat_1:
#        coordinat_2 += 1
#    elif answer == "s" or answer == "S" and coordinat_2 != stop_coordinat_2 and coordinat_2 != stop_coordinat_1:
#        coordinat_2 -= 1

coordinat_1 = 8
coordinat_2 = 10
stop_coordinat_min = 0
stop_coordinat_width_max = 15
stop_coordinat_max = 20

while True:
    print("Марсоход находится на позиции:", coordinat_1, coordinat_2, "введите команду:")
    answer = input(" ")

    if answer == "a" or answer == "A":
        if coordinat_1 > stop_coordinat_min:
            coordinat_1 -= 1
    elif answer == "d" or answer == "D":
        if coordinat_1 < stop_coordinat_width_max:
            coordinat_1 += 1
    elif answer == "w" or answer == "W":
        if coordinat_2 < stop_coordinat_max:
            coordinat_2 += 1
    elif answer == "s" or answer == "S":
        if coordinat_2 > stop_coordinat_min:
            coordinat_2 -= 1
    else:
        print("Неправильное значение!")