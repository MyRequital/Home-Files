text = input("Введите фразу: ")
first_sym = "Ы"
second_sym = "ы"
first_sym_count = 0
second_sym_count = 0
for phrase in text:
    if phrase == first_sym:
        first_sym_count += 1
    if phrase == second_sym:
        second_sym_count += 1
print("Кол-во букв", first_sym, "=", first_sym_count)
print("Кол-во букв", second_sym, "=", second_sym_count)

