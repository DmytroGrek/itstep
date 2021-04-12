# Напишіть клас OrcArmy, який містить такі поля (повинні задаватися при ініціалізації):
#          a.  warrior amount
#          b.  damage per warrior
#          c.  warrior health
# Реалізуйте перегрузку арифметичних операторів для операцій + та -. При додаванні створюється новий об’єкт в
# якому warrior amount це сума двох значень кількість бійців кожного об’єкту, які сумуються, damage per orc стає зважене
# середнє арифметичне (але вам потрібно враховувати скільки було орків в кожній армії, щоб вирахувати його
# вірно) та warrior health також середнє арифметичне. В разі віднімання ми віднімаємо кількість воїнів, якщо число рівне
# або менше нуля то повертається армія без воїнів(warrior amount = 0)
class OrcArmy:
    def __init__(self, warrior_amount, damage_per_orc, warrior_health):
        self.warrior_amount = warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health

    def __str__(self):
        return f'{self.warrior_amount} {self.damage_per_orc} {self.warrior_health}'

    def __add__(self, other):
        new_amount = self.warrior_amount + other.warrior_amount
        new_damage = (self.warrior_amount * self.damage_per_orc + other.warrior_amount * other.damage_per_orc) /\
                     (self.warrior_amount + other.warrior_amount)
        new_health = (self.warrior_amount * self.warrior_health + other.warrior_amount * other.warrior_health) /\
                     (self.warrior_amount + other.warrior_amount)
        return OrcArmy(new_amount, round(new_damage, 2), round(new_health, 2))

    def __sub__(self, other):
        sub = self.warrior_amount - other.warrior_amount
        return OrcArmy(0 if sub <= 0 else sub, self.damage_per_orc, self.warrior_health)


if __name__ == "__main__":
    enemy = OrcArmy(0, 15, 5)
    enemy_1 = OrcArmy(55, 20, 17)
    big_enemy = enemy + enemy_1
    print(big_enemy)
    down_enemy = enemy - enemy_1
    print(down_enemy)
