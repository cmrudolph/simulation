from owl import Game, Hand, Card, Color
import strategies


class Game(Game):
    @property
    def front(self):
        return self.occupied[2]

    @property
    def middle(self):
        return self.occupied[1]

    @property
    def back(self):
        return self.occupied[0]


def test_back_owl_random_card():
    def fixed_random(start, end):
        return 1

    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|1    |     |     |     |     |     |
    #    v---^
    g = Game(3)
    h = Hand()
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    red = Card.create_colored(Color.red)
    h.add(blue)
    h.add(purple)
    h.add(red)

    choice = strategies.back_owl_random_card(g, [h], 0, fixed_random)
    assert choice == (g.back, h.cards[1])


def test_random_owl_random_card():
    def fixed_random(start, end):
        return 1

    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|1    |     |     |     |     |     |
    #     v-----^
    g = Game(3)
    h = Hand()
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    red = Card.create_colored(Color.red)
    h.add(blue)
    h.add(purple)
    h.add(red)

    choice = strategies.random_owl_random_card(g, [h], 0, fixed_random)
    assert choice == (g.middle, h.cards[1])


def test_front_owl_random_card():
    def fixed_random(start, end):
        return 1

    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|1    |     |     |     |     |     |
    #       v-^
    g = Game(3)
    h = Hand()
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    red = Card.create_colored(Color.red)
    h.add(blue)
    h.add(purple)
    h.add(red)

    choice = strategies.front_owl_random_card(g, [h], 0, fixed_random)
    assert choice == (g.front, h.cards[1])


def test_back_owl_smallest_gain():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|  1  |     |     |     |     |     |
    #    v--^
    g = Game(3)
    g.move_owl(5, 7)
    h = Hand()
    red = Card.create_colored(Color.red)
    blue = Card.create_colored(Color.blue)
    h.add(red)
    h.add(blue)

    choice = strategies.back_owl_smallest_gain(g, [h], 0, None)
    assert choice == (g.back, red)


def test_any_owl_smallest_gain():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|   1 |     |     |     |     |     |
    #     v-^
    g = Game(3)
    g.move_owl(5, 8)
    h = Hand()
    red = Card.create_colored(Color.red)
    blue = Card.create_colored(Color.blue)
    h.add(red)
    h.add(blue)

    choice = strategies.any_owl_smallest_gain(g, [h], 0, None)
    assert choice == (g.middle, red)


def test_front_owl_smallest_gain():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|   1 |     |     |     |     |     |
    #          v^
    g = Game(3)
    g.move_owl(5, 8)
    h = Hand()
    yellow = Card.create_colored(Color.yellow)
    green = Card.create_colored(Color.green)
    h.add(yellow)
    h.add(green)

    choice = strategies.front_owl_smallest_gain(g, [h], 0, None)
    assert choice == (g.front, yellow)


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

    choice = strategies.back_owl_biggest_gain(g, [h], 0, None)
    assert choice == (g.back, blue)


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

    choice = strategies.any_owl_biggest_gain(g, [h], 0, None)
    assert choice == (g.front, blue)


def test_front_owl_biggest_gain():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|  1  |     |     |     |     |     |
    #         v----^
    g = Game(3)
    g.move_owl(5, 7)
    h = Hand()
    red = Card.create_colored(Color.red)
    yellow = Card.create_colored(Color.yellow)
    h.add(red)
    h.add(yellow)

    choice = strategies.front_owl_biggest_gain(g, [h], 0, None)
    assert choice == (g.front, yellow)


def test_back_owl_color_priority():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|   1 |     |     |     |     |     |
    #    v----^
    g = Game(3)
    g.move_owl(5, 8)
    h = Hand()
    red = Card.create_colored(Color.red)
    blue = Card.create_colored(Color.blue)
    purple = Card.create_colored(Color.purple)
    h.add(red)
    h.add(blue)
    h.add(purple)

    choice = strategies.back_owl_color_priority(g, [h], 0, None)
    assert choice == (g.back, blue)


def test_front_owl_color_priority():
    # YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP
    #    32|    1|     |     |     |     |     |
    #           v--^
    g = Game(3)
    g.move_owl(5, 9)
    h = Hand()
    green = Card.create_colored(Color.green)
    blue = Card.create_colored(Color.blue)
    orange = Card.create_colored(Color.orange)
    h.add(green)
    h.add(blue)
    h.add(orange)

    choice = strategies.front_owl_color_priority(g, [h], 0, None)
    assert choice == (g.front, blue)
