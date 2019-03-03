from owl import Card, Color, play, first_owl_first_card


def test_all_suns():
    def draw():
        yield Card.create_sun()

    print()
    play(3, 2, lambda: next(draw()), first_owl_first_card)

def test_no_suns():
    def draw():
        yield Card.create_colored(Color.red)

    print()
    play(3, 2, lambda: next(draw()), first_owl_first_card)
