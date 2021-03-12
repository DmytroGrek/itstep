# Гаррі та Рон почали підготовку, але як завжди не обійшлися без допомогти їх вірної подруги Герміони,
# яка почала вчити їх новим заклинанням. Допоможіть розширити набір заклинань, хлопців та напишіть
# функцію add_new_spell(spells_list: set, new_spell: str) -> bool. Функція приймає set заклинань
# та назву нового заклинання, якого хоче навчити Герміона. Функція розширює поточний список та повертає True,
# в разі якщо це нове заклинання і просто повертає False, якщо це заклинання вже є в наборі.
# >>> add_new_spell(Ron, “Expelliarmus”)
# True
# >>> print(Ron)
# {“Accio”, “Wingardium Leviosa”, “Alohomora”, “Expelliarmus”}
# >>> add_new_spell(Harry, “Expelliarmus”)
# False
# >>> print(Harry)
# {“Accio”, “Wingardium Leviosa”, “Expelliarmus”, “Expecto patronum”}

Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}


def add_new_spell(spells_list: set, new_spell: str) -> bool:
    if new_spell not in spells_list:
        spells_list.add(new_spell)
        return True
    else:
        return False


print(add_new_spell(Ron, 'Expelliarmus'))
print(Ron)
print(add_new_spell(Harry, 'Expelliarmus'))
print(Harry)
