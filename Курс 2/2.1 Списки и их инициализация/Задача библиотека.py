books_id = [50, 34, -1, -1, 2, 23, -1]
new_books_id = []
returned = 0

for _ in range(10):
    id = int(input("Введите ID книги: "))
    books_id.append(id)

for i_id in books_id:
    if i_id == -1:
        returned += 1
    else:
        new_books_id.append(i_id)

print(f"Новый список выданных книг = {new_books_id}"
      f"\nВернули за день: {returned}")