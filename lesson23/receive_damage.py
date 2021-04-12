# Розширте попередній клас та додайте методи, пошкодження та атаки.
# Метод receive_damage(damage: int) приймає число скільки одиниць пошкодження на них кидають та
# повертає число своїх воїнів, що померли, а також оновлює поле з кількістю воїнів в армії (warrior amount).
# А прорахувати скільки воїнів померло можна за допомогою ділення атаки на параметр warrior health,
# що вказує скільки одиниць життя має один воїн.
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

    def receive_damage(self, damage: int):
        damage = damage // self.warrior_health
        self.warrior_amount = self.warrior_amount - damage
        if self.warrior_amount <= 0:
            self.warrior_amount = 0


if __name__ == "__main__":
    enemy = OrcArmy(70, 15, 5)
    enemy_1 = OrcArmy(155, 20, 17)
    big_enemy = enemy + enemy_1
    print(big_enemy)
    down_enemy = enemy - enemy_1
    print(down_enemy)
    enemy.receive_damage(300)
    print(enemy)
    print(enemy.receive_damage(150))
