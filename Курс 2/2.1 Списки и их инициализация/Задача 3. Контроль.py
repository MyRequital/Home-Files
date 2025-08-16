number_employees = int(input("Введите кол-во сотрудников: "))
id_active_employees = []
for i in range(number_employees):
    input_active_user_id = int(input("ID сотрудника: "))
    id_active_employees.append(input_active_user_id)
search_id = int(input("Какой ID ищем?: "))
if search_id in id_active_employees:
    print("Сотрудник работает!")
else:
    print("Сотрудник не работает!")