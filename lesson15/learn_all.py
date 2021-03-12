# Хлопці вирішили навчити один одного тих заклинань, що вони знають. Напишіть функцію
# learn_all(my_spells: set, teacher_spells: set) -> set. Функція приймає набір заклинань
# того хто вчить та того хто навчає, а у відповідь повертає множину всіх заклинань, які буде знати після
# того, як навчиться всіх нових від свого вчителя.
# >>> learn_all(Ron, Harry)
# {“Accio”, “Wingardium Leviosa”, “Alohomora”, “Expelliarmus”, “Expecto patronum”}

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}


def learn_all(my_spells: set, teacher_spells: set) -> set:
    return my_spells.union(teacher_spells)
    # return my_spells | teacher_spells     # для себя


print(learn_all(Ron, Harry))
