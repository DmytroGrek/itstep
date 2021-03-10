# Реалізувати функцію intersect(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple,
# яка приймає три кортежі з цілими числами та повертає кортеж зі значеннями які
# пересікаються у всіх наданих кортежах.
# >>> intersect((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1))   (2, 7)

def intersect(tup1, tup2, tup3):
    res = tuple(set(tup1) & set(tup2) & set(tup3))
    return res


print(intersect((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1)))
