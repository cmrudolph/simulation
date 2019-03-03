from owl import Game, Hand, Card, Color
import strategies


def test_first_owl_first_card():
    g = Game(3)
    h = Hand()
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    h.add(blue)
    h.add(purple)

    choice = strategies.first_owl_first_card(g, [h], 0)
    assert choice == (3, blue)


def test_first_owl_biggest_gain():
    g = Game(3)
    h = Hand()
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    h.add(blue)
    h.add(purple)

    choice = strategies.first_owl_biggest_gain(g, [h], 0)
    assert choice == (3, purple)
