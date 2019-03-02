import owl
from collections import Counter


def test_board():
    b = owl.Board(3)

    assert b.is_win() is False
    assert b.is_loss() is False
    assert b.get_occupied() == [3, 4, 5]

    print()
    b.print_state()


def test_win():
    b = owl.Board(3)

    b.move_owl(3, owl.NEST)
    b.move_owl(4, owl.NEST)
    assert b.is_win() is False

    b.move_owl(5, owl.NEST)
    assert b.is_win() is True


def test_loss():
    b = owl.Board(3)

    for i in range(12):
        b.add_sun()
    assert b.is_loss() is False

    b.add_sun()
    assert b.is_loss() is True


def test_color_query():
    b = owl.Board(3)

    assert b.color_at(0) == owl.Color.yellow
    assert b.color_at(38) == owl.Color.purple


def test_move():
    b = owl.Board(3)
    b.move_owl(3, 7)

    print()
    b.print_state()


def test_compute_end_no_obstacles():
    b = owl.Board(3)
    assert b.compute_end(5, owl.Color.blue) == 6
    assert b.compute_end(5, owl.Color.green) == 10


def test_compute_end_occupied():
    b = owl.Board(3)
    assert b.compute_end(3, owl.Color.purple) == 7
    assert b.compute_end(3, owl.Color.red) == 8


def test_compute_end_nest():
    b = owl.Board(3)
    assert b.compute_end(38, owl.Color.purple) == owl.NEST
    assert b.compute_end(38, owl.Color.red) == owl.NEST
