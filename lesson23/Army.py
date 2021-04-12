# Написати клас Army, для того щоб оптимізувати код. І від нього спадкувати класи OrcArmy та ElfArmy
class Army:
    def __init__(self, warrior_amount, damage_per_orc, warrior_health, shield=0):
        self.warrior_amount = warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health
        self.shield = shield

    def __str__(self):
        if not self.warrior_amount:
            return f'Army {self.__class__.__name__} is dead'
        return f'{self.__class__.__name__} {self.warrior_amount} {self.damage_per_orc} {self.warrior_health}' \
               f' {self.shield}'

    def __add__(self, other):
        new_amount = self.warrior_amount + other.warrior_amount
        new_damage = (self.warrior_amount * self.damage_per_orc + other.warrior_amount * other.damage_per_orc) /\
                     (self.warrior_amount + other.warrior_amount)
        new_health = (self.warrior_amount * self.warrior_health + other.warrior_amount * other.warrior_health) /\
                     (self.warrior_amount + other.warrior_amount)
        new_shield = (self.warrior_amount * self.shield + other.warrior_amount * other.shield) / \
                     (self.warrior_amount + other.warrior_amount)

        return self.__class__(new_amount, round(new_damage, 2), round(new_health, 2), round(new_shield, 2))

    def __sub__(self, other):
        sub = self.warrior_amount - other.warrior_amount
        return self.__class__(0 if sub <= 0 else sub, self.damage_per_orc, self.warrior_health, self.shield)

    def receive_damage(self, damage: int):
        damage = (damage - self.shield) // self.warrior_health
        self.warrior_amount = self.warrior_amount - damage
        if self.warrior_amount < 0:
            self.warrior_amount = 0


class ElfArmy(Army):

    def __init__(self, warrior_amount, damage_per_orc, warrior_health, shield):
        super().__init__(warrior_amount, damage_per_orc, warrior_health, shield)


class OrcArmy(Army):
    def __init__(self, warrior_amount, damage_per_orc, warrior_health, shield=0):
        super().__init__(warrior_amount, damage_per_orc, warrior_health)


if __name__ == "__main__":
    enemy = OrcArmy(70, 15, 5)
    enemy_1 = ElfArmy(155, 20, 17, 8)
    big_enemy = enemy_1 + enemy
    print(big_enemy)
    down_enemy = enemy - enemy_1
    print(down_enemy)
    enemy.receive_damage(100)
    print(enemy)
    print(enemy.receive_damage(50))
