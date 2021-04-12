# Напишіть програму army_destroy.py в якій створіть декілька армій кожного типу і об’єднайте їх в один
# список. Потім дайте користувачу вносити число на яку кількість одиниць атакувати одночасно всі армії. Після
# чого виводьте детальний звіт по кожній з армій (в разі якщо бійців в армії не залишилось відображати, що цю
# армію розбито)
from Army import OrcArmy, ElfArmy
enemy = OrcArmy(70, 15, 5)
enemy_1 = OrcArmy(85, 10, 7)
enemy_2 = ElfArmy(55, 20, 17, 8)
enemy_3 = ElfArmy(155, 25, 19, 9)
big_enemy = enemy + enemy_1
down_enemy = enemy_2 - enemy_3
enemy_list = [enemy, enemy_1, enemy_2, enemy_3, big_enemy, down_enemy]
while True:
    damage = input('Enter damage or e for exit: ')
    if damage == 'e':
        break
    if damage.isdigit():
        damage = int(damage)
        for i in enemy_list:
            i.receive_damage(damage)
        print(*enemy_list, sep='\n')
    else:
        print('Please use digit or e')
