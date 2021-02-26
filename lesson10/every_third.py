# пробовал варианты, можно так...импорт файла
# import even_list_generate as elg
#
#
# def every_third(start, end):
#     return elg.even_list_generate(start, end)[::3]

# или так, из файла импорт функции
from even_list_generate import even_list_generate as elg


def every_third(start, end):
    return elg(start, end)[::3]


print(every_third(1, 25))
