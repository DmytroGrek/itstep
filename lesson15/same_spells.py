# Для того щоб зрозуміти, які спільні заклинання знають хлопці напишіть
# функцію same_spells(ron_spells: set, harry_spells: set) -> set, яка приймає 2 множини з
# заклинаннями у вигляді рядків та повертає множину з заклинаннями, які знають обоє чаклунів.
# >>> Ron = {“Accio”, “Wingardium Leviosa”, “Alohomora”}
# >>> Harry = {“Accio”, “Wingardium Leviosa”, “Expelliarmus”, “Expecto patronum”}
# >>> same_spells(Ron, Harry)
# {“Accio”, “Wingardium Leviosa”}

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}


def same_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.intersection(harry_spells)
    # return ron_spells & harry_spells   # для себя


print(same_spells(Ron, Harry))
