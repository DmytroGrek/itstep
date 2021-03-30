# Реалізуйте клас Deck. Який містить параметр cards в якому знаходиться поточна карткова колода
# у вигляді списку з кортежів. Де перший елемент кортежа це ранг карти, а другий масть.
# Напишіть метод shuffle(), який буде перемішувати карти випадковим чином. Також напишіть метод
# take_card(), що приймає кортеж, який потрібно видалити з колоди. Тобто при ініціалізації
# клас вже містить колоду з картами, кожен виклик shuffle() перемішує поточну колоду.
# cards_example = [('A', 'Spades'), ('K', 'Clubs'), (10, 'Diamonds'), (5, 'Hearts')]
import random


class Deck:
    cards = [
        ('A', 'hearts'), (2, 'club'), ('A', 'diamond'), (3, 'hearts'), (6, 'diamond'), (7, 'hearts'), ('A', 'spade'),
        ('K', 'hearts'), (9, 'diamond'), (10, 'diamond'), ('Q', 'spade'), (2, 'spade'), (3, 'diamond'), (3, 'club'),
        (8, 'spade'), (4, 'spade'), (10, 'spade'), (8, 'club'), (6, 'hearts'), ('J', 'club'), (2, 'diamond'),
        (3, 'spade'), (9, 'hearts'), (10, 'hearts'), (8, 'hearts'), ('Q', 'diamond'), ('Q', 'hearts'), (7, 'diamond'),
        (4, 'hearts'), (5, 'hearts'), ('K', 'spade'), ('K', 'diamond'), (4, 'diamond'), (5, 'diamond'), (10, 'club'),
        ('A', 'club'), (9, 'spade'), (8, 'diamond'), ('J', 'spade'), (6, 'club'), ('K', 'club'), (7, 'spade'),
        ('J', 'diamond'), (5, 'club'), ('J', 'hearts'), (4, 'club'), (2, 'hearts'), ('Q', 'club'), (9, 'club'),
        (5, 'spade'), (6, 'spade'), (7, 'club')]

    def __init__(self, cards=None):
        if cards:
            self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self, value: tuple) -> None:
        if value in self.cards:
            self.cards.remove(value)
        else:
            print('There is no such card')


play = Deck()
play.shuffle()
print(play.cards)
play.take_card((2, 'spade'))
print(play.cards)
play.take_card((15, 'spade'))
