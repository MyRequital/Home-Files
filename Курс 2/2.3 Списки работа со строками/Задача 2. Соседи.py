"""
Дана строка S и номер позиции символа в строке. Напишите программу,
которая выводит соседей этого символа и сообщение о количестве таких же символов среди этих соседей:
их нет, есть ровно один или есть два таких же.
"""

text = input("Введите строку: ")
symbol_user = int(input("Введите номер символа: ")) - 1
count = 0
text_list = list(text)

print(f"выбранная буква: {text_list[symbol_user]}")

if symbol_user < 1:
    print("Неверный номер символа!")
elif symbol_user > len(text_list):
    print("Неверный номер символа!")
elif symbol_user == 1:
    print(f"Символ слева: пустой")
    print(f"Символ справа {text_list[symbol_user + 1]}")
    if text_list[symbol_user] == text_list[symbol_user + 1]:
        count += 1
elif symbol_user == len(text_list) - 1:
    print(f"Символ слева: {text_list[symbol_user - 1]}")
    print("Символ справа: пустой")
    if text_list[symbol_user] == text_list[symbol_user - 1]:
        count += 1
else:
    print(f"Символ слева: {text_list[symbol_user - 1]}")
    print(f"Символ справа {text_list[symbol_user + 1]}")
    if text_list[symbol_user] == text_list[symbol_user + 1]:
        count += 1
    if text_list[symbol_user] == text_list[symbol_user - 1]:
        count += 1

if count == 1:
    print("Есть ровно один такой же символ")
elif count == 2:
    print("Есть ровно два таких же символов")
else:
    print("Таких же символов нет!")