from owl import Color, Game, NEST
from collections import Counter


def test_game():
    g = Game(3)

    assert g.is_win() is False
    assert g.is_loss() is False
    assert g.get_occupied() == [3, 4, 5]

    print()
    g.print_state()


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


def test_color_query():
    g = Game(3)

    assert g.color_at(0) == Color.yellow
    assert g.color_at(38) == Color.purple


def test_move():
    g = Game(3)
    g.move_owl(3, 7)

    print()
    g.print_state()


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
