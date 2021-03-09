# Написать программу «справочник». Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
# ■ Отсортировать по идентификационным кодам;
# ■ Отсортировать по номерам телефона;
# ■ Вывести список пользователей с кодами и телефонами;
# ■ Выход.
id_code = ['045', '047', '039', '123']
numbers = ['0932328998', '0671831758', '0684655545', '0503221866']
handbook = list(zip(id_code, numbers))
print(handbook)

while True:
    choose = input(
            "Make your choose:\n"
            "Sort by id code, enter - 1\n"
            "Sort by phone number, enter - 2\n"
            "List of users with id code and phone numbers, enter - 3\n"
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
        sorted(id_code)
        print('The list is sorted by id code')
        print([i[0] for i in sorted(handbook, key=lambda x: x[0])])  # из условия непонятно надо это или нет
    elif choose == 2:
        sorted(numbers)
        print('The list is sorted by phone number')
        print([i[1] for i in sorted(handbook, key=lambda x: x[1])])  # из условия непонятно надо это или нет
        print(handbook)
