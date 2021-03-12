# Герміона почала настільки швидко навчати, що додавати в список по одному задовго, розширте
# попередню функцію, щоб вони приймала скільки завгодно назв заклинань і додавала їх та повертала True
# тільки в разі якщо всі заклинання не зустрічаються в наданому наборі заклинань чаклуна. Нову функцію
# назвіть add_new_spells(...) -> bool
# >>> add_new_spells(Harry, “Expelliarmus”, “Lumos”, “Obliviate”)
# False
# >>> print(Harry)
# {“Accio”, “Wingardium Leviosa”, “Expelliarmus”, “Expecto patronum”}

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}


def add_new_spells(spells_list: set, *new_spell) -> bool:
    if spells_list.isdisjoint(new_spell):
        for i in new_spell:
            spells_list.add(i)
        return True
    else:
        return False


print(add_new_spells(Harry, 'Expelliarmus', 'Lumos', 'Obliviate'))
print(Harry)
