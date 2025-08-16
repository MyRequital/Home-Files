x_lim = 50
y_lim = 20

for y in range(y_lim):
    for x in range(x_lim):
        if x == x_lim // 2:
            print('|', end='')
        elif x == y + 31:
            print("\\", end = "")
        elif y == 7:
            print("-", end = "")
        elif y == 8 and x < x_lim or y == 9 and x < x_lim:
            print("|", end = "")
        elif x == -y + 19:
            print("/", end = "")
        elif y == y_lim // 2:
            print('-', end='')
        else:
            print(' ', end='')
    print()
