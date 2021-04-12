# Напишіть клас ElfArmy, він не успадковується від попереднього класу, це свій незалежний клас. Він має
# спільні параметри, що і в класі OrcArmy за виключенням додаткового параметру shield. Який дає
# перевагу цій армії перед армію Орків. В цьому класі при вирахуванні методу receive_damage()
# перед тим як починати рахувати померлих воїнів, потрібно відняти від атаки параметр shield який вказує
# на скільки одиниць армія відражає атаку без втрат.
class ElfArmy:
    def __init__(self, warrior_amount, damage_per_orc, warrior_health, shield):
        self.warrior_amount = warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health
        self.shield = shield

    def __str__(self):
        return f'{self.warrior_amount} {self.damage_per_orc} {self.warrior_health} {self.shield}'

    def __add__(self, other):
        new_amount = self.warrior_amount + other.warrior_amount
        new_damage = (self.warrior_amount * self.damage_per_orc + other.warrior_amount * other.damage_per_orc) /\
                     (self.warrior_amount + other.warrior_amount)
        new_health = (self.warrior_amount * self.warrior_health + other.warrior_amount * other.warrior_health) /\
                     (self.warrior_amount + other.warrior_amount)
        new_shield = (self.warrior_amount * self.shield + other.warrior_amount * other.shield) / \
                     (self.warrior_amount + other.shield)

        return ElfArmy(new_amount, round(new_damage, 2), round(new_health, 2), round(new_shield, 2))

    def __sub__(self, other):
        sub = self.warrior_amount - other.warrior_amount
        return self.__class__(0 if sub <= 0 else sub, self.damage_per_orc, self.warrior_health, self.shield)

    def receive_damage(self, damage: int):
        damage = (damage - self.shield) // self.warrior_health
        self.warrior_amount = self.warrior_amount - damage
        if self.warrior_amount < 0:
            self.warrior_amount = 0


if __name__ == "__main__":
    enemy = ElfArmy(70, 15, 5, 7)
    enemy_1 = ElfArmy(55, 20, 17, 8)
    big_enemy = enemy + enemy_1
    print(big_enemy)
    down_enemy = enemy - enemy_1
    print(down_enemy)
    enemy.receive_damage(100)
    print(enemy)
    print(enemy.receive_damage(50))
