# Реалізувати функцію same_pos(tup1: tuple, tup2: tuple, tup3: tuple) -> dict,
# яка приймає три кортежі з цілими числами та повертає словник зі значеннями які
# пересікаються у всіх наданих кортежах та на тих же позиціях. В словнику під ключем
# має бути значення а під значенням індекс позицію де число стоїть у всіх кортежах.
# >>> same_pos((4, 2, 6, 7), (1, 2, 7, 7), (2, 2, 2, 7, 1))
#    {2: 1, 7: 3}

def same_pos(tup1, tup2, tup3):
    result = {}
    args = sorted((tup1, tup2, tup3), key=lambda x: len(x))

    for index, elem in enumerate(args[0]):
        if elem == args[1][index] == args[2][index]:
            result[elem] = index
    return result


print(same_pos((4, 2, 6, 7), (1, 2, 7, 7), (2, 2, 2, 7, 1)))
