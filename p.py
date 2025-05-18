import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        print('hi')
        return len(self._cards)

    def __getitem__(self, position):
        print('hi')
        return self._cards[position]


deck = FrenchDeck()
print(
    deck[-1]
)
