from owl import Color, Game, NEST
from collections import Counter


def test_game_init():
    g = Game(3)

    assert g.is_win() is False
    assert g.is_loss() is False
    assert g.suns == 0
    assert g.get_occupied() == [3, 4, 5]


def test_win():
    g = Game(3)

    g.move_owl(3, NEST)
    g.move_owl(4, NEST)
    assert g.is_win() is False

    g.move_owl(5, NEST)
    assert g.is_win() is True


def test_loss():
    g = Game(3)

    for i in range(12):
        g.add_sun()
    assert g.is_loss() is False

    g.add_sun()
    assert g.is_loss() is True


def test_trace():
    g = Game(3, capture_trace=True)

    g.add_sun()
    g.move_owl(3, 10)
    g.move_owl(4, 15)
    g.move_owl(5, NEST)

    print()
    print(g.get_trace())

    expected = (
        "YGOBP|RBPRY|GBORP|YGOBP|RGYOB|PRYGB|ORPYG|BORP\n" +
        "   32|1    |     |     |     |     |     |     || N:0 S:1\n" +
        "    2|1    |3    |     |     |     |     |     || N:0 S:1\n" +
        "     |1    |3    |2    |     |     |     |     || N:0 S:1\n" +
        "     |     |3    |2    |     |     |     |     || N:1 S:1\n" +
        "Won:False; Loss:False; Act:4; Sun:1; Owls:2"
    )
    assert g.get_trace() == expected


def test_color_query():
    g = Game(3)

    assert g.color_at(0) == Color.yellow
    assert g.color_at(38) == Color.purple


def test_move_owl():
    g = Game(3)
    g.move_owl(3, 7)

    assert g.get_occupied() == [4, 5, 7]


def test_compute_end_no_obstacles():
    g = Game(3)
    assert g.compute_end(5, Color.blue) == 6
    assert g.compute_end(5, Color.green) == 10


def test_compute_end_occupied():
    g = Game(3)
    assert g.compute_end(3, Color.purple) == 7
    assert g.compute_end(3, Color.red) == 8


def test_compute_end_nest():
    g = Game(3)
    assert g.compute_end(38, Color.purple) == NEST
    assert g.compute_end(38, Color.red) == NEST
