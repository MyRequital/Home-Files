uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
phone = ''
for ch in uph:
    if ch == '+' or ('0' <= ch <= '9'):
        print('0' <= ch <= '9')
        phone += ch

print(phone)