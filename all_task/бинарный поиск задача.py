beginning_segment = 1
end_segment = 100
midpoint = 1
while True:
    midpoint = (beginning_segment + end_segment) // 2
    print('Загаданное число равно, меньше или больше', midpoint)
    answer = int(input('1 - равно, 2 - больше, 3 - меньше '))
    if answer == 1:
        print("Я угадал!")
        break
    if answer == 2:
        beginning_segment = midpoint
    elif answer == 3:
        end_segment = midpoint
