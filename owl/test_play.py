from owl import Card, Color, play
import strategies


def test_all_suns():
    def draw():
        yield Card.create_sun()

    strategy = strategies.back_owl_first_card
    result = play(3, 2, lambda: next(draw()), strategy)

    assert result.owls == 3
    assert result.players == 2
    assert result.actions == 13
    assert result.strategy == "back_owl_first_card"
    assert result.suns == 13
    assert result.won is False


def test_no_suns():
    def draw():
        yield Card.create_colored(Color.red)

    strategy = strategies.back_owl_first_card
    result = play(3, 2, lambda: next(draw()), strategy)

    assert result.owls == 3
    assert result.players == 2
    assert result.actions == 9
    assert result.strategy == "back_owl_first_card"
    assert result.suns == 0
    assert result.won is True
