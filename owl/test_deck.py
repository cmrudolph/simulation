from owl import Deck
from collections import Counter


def test_deck():
    d1 = Deck()
    d2 = Deck()

    cards1 = []
    cards2 = []
    for i in range(50):
        cards1.append(d1.draw())
        cards2.append(d2.draw())

    counter1 = Counter(cards1)
    counter2 = Counter(cards2)

    assert cards1 != cards2
    assert counter1 == counter2
