from owl import Game, Hand, Card, Color
import strategies


def test_back_owl_first_card():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|1    |     |     |     |     |     |
    #    v---^
    g = Game(3)
    h = Hand()
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    h.add(blue)
    h.add(purple)

    choice = strategies.back_owl_first_card(g, [h], 0)
    assert choice == (3, blue)


def test_back_owl_biggest_gain():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|  1  |     |     |     |     |     |
    #    v---^
    g = Game(3)
    g.move_owl(5, 7)
    h = Hand()
    red = Card.create_colored(Color.red)
    blue = Card.create_colored(Color.blue)
    h.add(red)
    h.add(blue)

    choice = strategies.back_owl_biggest_gain(g, [h], 0)
    assert choice == (3, blue)


def test_any_owl_biggest_gain():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|  1  |     |     |     |     |     |
    #         v----^
    g = Game(3)
    g.move_owl(5, 7)
    h = Hand()
    red = Card.create_colored(Color.red)
    blue = Card.create_colored(Color.blue)
    h.add(red)
    h.add(blue)

    choice = strategies.any_owl_biggest_gain(g, [h], 0)
    assert choice == (7, blue)
