# Так, same_spells допомогло хлопцям зрозуміти, в чому вони і так майстри і звертати увагу
# на ці заклинання не потрібно, але є заклинання, які знає лише один з них. Якщо вони дізнаються
# такі заклинання то просто зможуть навчити один одного і стати, ще більш крутими чарівниками.
# unique_spells(ron_spells: set, harry_spells: set) -> set, яка приймає 2 множини з заклинаннями у
# вигляді рядків та повертає множину з заклинаннями, які знає лише один з юних чаклунів.
# >>> unique_spells(Ron, Harry)
# {“Alohomora”, “Expelliarmus”, “Expecto patronum”}

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}


def unique_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.symmetric_difference(harry_spells)
    # return set(ron_spells) ^ set(harry_spells)   # для себя


print(unique_spells(Ron, Harry))
