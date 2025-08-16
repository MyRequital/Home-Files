
x_lim = 50
y_lim = 20

for y in range(y_lim):
    for x in range(x_lim):
        if x == x_lim // 2:  # Ключевое отличие в порядке проверок. Если сперва выполняется проверка на дефис, то именно дефис будет выбран.
            print('|', end='')
        elif y == y_lim // 2:
            print('-', end='')
        else:
            print(' ', end='')
    print()