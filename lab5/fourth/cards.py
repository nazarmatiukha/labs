import random


class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def info_rank(self):
        return self.rank

    def __str__(self):
        return f'{self.rank} {self.suit}'


class CardsDeck:

    def __init__(self, cards):
        self.cards = cards

    def deck_info(self):
        for card in self.cards:
            print(card)

    def mix_card(self):
        random.shuffle(self.cards)

    def one_card(self):
        if not self.cards:
            return 'no card'
        return random.choice(self.cards)

    def six_card(self):
        return [self.one_card() for _ in range(6)]


rank = ['Туз', 'Король', 'Дама', 'Валет', '10', '9', '8', '7', '6', ]
suit = ["червей", "бубей", "крестей", "пик"]
cards = [Cards(s, r) for s in suit for r in rank]

deck = CardsDeck(cards)
print('Колода:')
deck.deck_info()
deck.mix_card()
print()
print('Перемешанная колода:')
deck.deck_info()
print()
print('Выдача одной карты:')
print(deck.one_card())
print()
print('Выдача 6 карт:')
for card in deck.six_card():
    print(card)
deck.get(int(input('Введите карту для поиска')))
