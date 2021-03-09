# Написать программу «книги». Создать два списка
# с данными. Один список хранит названия книг, второй —
# годы выпуска. Реализовать меню для пользователя:
# ■ Отсортировать по названию книг;
# ■ Отсортировать по годам выпуска;
# ■ Вывести список книг с названиями и годами выпуска;
# ■ Выход
books = ['Мастер и Маргарита', 'Евгений Онегин', 'Война и мир', 'Преступление и наказание']
years = [1937, 1831, 1865, 1866]
book_years = list(zip(books, years))

while True:
    choose = input(
            "Make your choose:\n"
            "Sort by book title, enter - 1\n"
            "Sort by year of issue, enter - 2\n"
            "List books with titles and years of release, enter - 3\n"
            "Exit, enter - 4: \n"
    )

    try:
        choose = int(choose)
        if 1 > choose or choose > 4:
            print('Please input digit from 1 to 4')
    except ValueError:
        print('Please input digit')
        continue

    if choose == 4:
        break

    if choose == 1:
        sorted(books)
        print('The list is sorted by book title')
        print([i[0] for i in sorted(book_years, key=lambda x: x[0])])  # из условия непонятно надо это или нет
    elif choose == 2:
        sorted(years)
        print('The list is sorted by year of issue')
        print([i[1] for i in sorted(book_years, key=lambda x: x[1])])  # из условия непонятно надо это или нет
    elif choose == 3:
        print(book_years)
