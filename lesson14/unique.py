# Реалізувати функцію unique(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple,
# яка приймає три кортежі з цілими числами та повертає кортеж з унікальними значеннями.
# >>> unique((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1))
# (4, 6, 9)

def unique(a, b, c):
    res = set(a) & set(b)
    res1 = set(a) & set(c)
    res2 = set(b) & set(c)
    res3 = set(a) | set(b) | set(c)
    result = res3 - (res | res1 | res2)
    return tuple(sorted(result))


print(unique((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1)))
