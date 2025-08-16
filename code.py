
import datetime
import os

class Expense:
    def __init__(self, amount, date, description=""):
        self.amount = amount
        self.date = date  # datetime.date
        self.description = description

    def __str__(self):
        return f"{self.date}: {self.description} - {self.amount} руб."

class MaterialExpense(Expense):
    def __init__(self, amount, date, material_name, description=""):
        super().__init__(amount, date, description)
        self.material_name = material_name

    def __str__(self):
        return f"{self.date} | Материал: {self.material_name} | {self.description} | Сумма: {self.amount} руб."

class LaborExpense(Expense):
    def __init__(self, amount, date, worker_name, description=""):
        super().__init__(amount, date, description)
        self.worker_name = worker_name

    def __str__(self):
        return f"{self.date} | Зарплата: {self.worker_name} | {self.description} | Сумма: {self.amount} руб."

class Income:
    def __init__(self, amount, date, description=""):
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date}: {self.description} - {self.amount} руб."

class Project:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.material_expenses = []
        self.labor_expenses = []
        self.incomes = []
        self.receipt_photos = []  # пути к фотографиям чеков

    def add_material_expense(self, amount, date, material_name, description=""):
        expense = MaterialExpense(amount, date, material_name, description)
        self.material_expenses.append(expense)
        print("Добавлены затраты на материалы.")

    def add_labor_expense(self, amount, date, worker_name, description=""):
        expense = LaborExpense(amount, date, worker_name, description)
        self.labor_expenses.append(expense)
        print("Добавлены затраты на зарплатный проект рабочих.")

    def add_income(self, amount, date, description=""):
        income = Income(amount, date, description)
        self.incomes.append(income)
        print("Добавлены поступления средств от заказчика.")

    def add_receipt_photo(self, filepath):
        if os.path.isfile(filepath):
            self.receipt_photos.append(filepath)
            print("Фото чека добавлено.")
        else:
            print("Файл не найден. Проверьте путь.")

    def total_material_expenses(self):
        return sum(e.amount for e in self.material_expenses)

    def total_labor_expenses(self):
        return sum(e.amount for e in self.labor_expenses)

    def total_expenses(self):
        return self.total_material_expenses() + self.total_labor_expenses()

    def total_incomes(self):
        return sum(i.amount for i in self.incomes)

    def balance(self):
        return self.total_incomes() - self.total_expenses()

    def print_summary(self):
        print(f"\nПроект: {self.name}")
        print(f"Бюджет: {self.budget} руб.")
        print(f"Общие затраты на материалы: {self.total_material_expenses()} руб.")
        print(f"Общие затраты на зарплату: {self.total_labor_expenses()} руб.")
        print(f"Общие затраты: {self.total_expenses()} руб.")
        print(f"Поступления от заказчика: {self.total_incomes()} руб.")
        print(f"Баланс (поступления - затраты): {self.balance()} руб.")
        print(f"Количество загруженных фото чеков: {len(self.receipt_photos)}")

    def print_details(self):
        print("\nДетали затрат на материалы:")
        for e in self.material_expenses:
            print(" -", e)
        print("\nДетали затрат на зарплату:")
        for e in self.labor_expenses:
            print(" -", e)
        print("\nПоступления от заказчика:")
        for i in self.incomes:
            print(" -", i)
        print("\nФотографии чеков:")
        for photo in self.receipt_photos:
            print(" -", photo)


def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты. Используйте ГГГГ-ММ-ДД.")
        return None


def main():
    print("=== Программа расчёта затрат на проект ===")
    name = input("Введите наименование объекта: ")
    while True:
        try:
            budget = float(input("Введите смету объекта (бюджет) в рублях: "))
            break
        except ValueError:
            print("Пожалуйста, введите число.")

    project = Project(name, budget)

    while True:
        print("\nВыберите действие:")
        print("1 - Добавить затраты на материалы")
        print("2 - Добавить затраты на зарплатный проект рабочих")
        print("3 - Добавить поступления от заказчика")
        print("4 - Добавить фото чека")
        print("5 - Показать сводку проекта")
        print("6 - Показать детали проекта")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            material_name = input("Введите наименование материала: ")
            amount_str = input("Введите сумму затрат на материалы: ")
            date_str = input("Введите дату затрат (ГГГГ-ММ-ДД): ")
            description = input("Описание (не обязательно): ")

            date = parse_date(date_str)
            if date is None:
                continue

            try:
                amount = float(amount_str)
            except ValueError:
                print("Неверная сумма.")
                continue

            project.add_material_expense(amount, date, material_name, description)

        elif choice == "2":
            worker_name = input("Введите имя рабочего: ")
            amount_str = input("Введите сумму зарплаты: ")
            date_str = input("Введите дату выплаты зарплаты (ГГГГ-ММ-ДД): ")
            description = input("Описание (не обязательно): ")

            date = parse_date(date_str)
            if date is None:
                continue

            try:
                amount = float(amount_str)
            except ValueError:
                print("Неверная сумма.")
                continue

            project.add_labor_expense(amount, date, worker_name, description)

        elif choice == "3":
            amount_str = input("Введите сумму поступления от заказчика: ")
            date_str = input("Введите дату поступления (ГГГГ-ММ-ДД): ")
            description = input("Описание (не обязательно): ")

            date = parse_date(date_str)
            if date is None:
                continue

            try:
                amount = float(amount_str)
            except ValueError:
                print("Неверная сумма.")
                continue

            project.add_income(amount, date, description)

        elif choice == "4":
            filepath = input("Введите путь к фото чека: ")
            project.add_receipt_photo(filepath)

        elif choice == "5":
            project.print_summary()

        elif choice == "6":
            project.print_details()

        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
