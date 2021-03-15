# def same_cities(a, b):
#     res = set(a) & set(b)
#     return res
#
#
# mark_cities = {'Boston', 'Lisbon', 'Paris', 'London'}
# peter_cities = {'New York', 'Lisbon', 'Michigan', 'London'}
# print(same_cities(mark_cities, peter_cities))
# {“Lisbon”, “London”}

# Наданий певний список з унікальними ідентифікаторами (цілі числа),
# які можуть повторюватися, ваша задача визначити лише унікальні значення
# та повернути список з ними, де відсутні повтори.
# Напишіть функцію unique_ids(ids: list) -> list яка все це зробить.
# >>> unique_ids([1, 2, 3, 4, 5, 2, 3, 4, 7, 8, 9, 8, 12, 13, 14, 14, 19]
# [1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 14, 19]


# def unique_ids(ids):
#     res = list(set(ids))
#     return res
#
#
# temp = unique_ids([1, 2, 3, 4, 5, 2, 3, 4, 7, 8, 9, 8, 12, 13, 14, 14, 19])
# print(unique_ids(temp))
#
mark_cities = {'Boston', 'Lisbon', 'Paris', 'London'}
peter_cities = {'New York', 'Lisbon', 'Michigan', 'London'}


def same_cities(a, b):

    while True:
        choose = input(
                "Make your choose:\n"
                "intersection cities, enter - 1\n"
                "unique cities for Mark, enter - 2\n"
                "unique cities for Peter, enter - 3\n"
                "union cities for Peter and Mark, enter - 4\n"
                "Exit, enter - exit: \n"
        ).lower()
        if choose == 'exit':
            break
        try:
            choose = int(choose)
            if 1 > choose or choose > 4:
                print('Please input digit from 1 to 4')
        except ValueError:
            print('Please input digit')
            continue

        if choose == 1:
            print('intersection cities', list(set(a) & set(b)))

        elif choose == 2:
            print('unique cities for Mark', list(set(a) - set(b)))

        elif choose == 3:
            print('unique cities for Peter', list(set(b) - set(a)))

        elif choose == 4:
            print('union cities for Peter and Mark', list(set(a) | set(b)))


print(same_cities(mark_cities, peter_cities))
