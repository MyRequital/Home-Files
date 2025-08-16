"""
В одной компании наступили «тёмные времена», и сотрудников стали сокращать.
Зарплаты сотрудников хранятся в списке из N этих самых зарплат.
Зарплаты уже уволенных сотрудников обозначаются в списке числом 0.

Напишите программу, которая запрашивает у пользователя количество сотрудников и их зарплаты,
затем удаляет все элементы списка со значением 0 и выводит в консоль, сколько сотрудников осталось,
а также их зарплаты. Дополнительный список использовать нельзя.
"""

employees_salaries = []
salary_list = []
number_employees = int(input("Введите кол-во сотрудников: "))

for i in range(number_employees):
    name, salary = input("Введите имя и зп сотрудника(Через пробел): ").split(" ")
    employees_salaries.append([name, salary])

print(f"Список сотрудников и их зарплаты: {employees_salaries}")

for idx, name_salary in enumerate(employees_salaries):
    name, salary = name_salary
    salary_list.append(salary)
    if int(salary) == 0:
        employees_salaries.remove(name_salary)

print(f"Список работников и их зарплат после сокращения: {employees_salaries}"
      f"\nМаксимальная зарплата сотрудника: {max(salary_list)}")

