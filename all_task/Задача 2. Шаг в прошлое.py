total_year = int(input("Введите год (не меньше 1900): "))
if total_year < 1900:
    print("Год должен быть не меньше 1900!")
for year in range(total_year, 1899, -2):
    print(year)
