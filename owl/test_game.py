import owl
from collections import Counter


def test_game():
    g = owl.Game(3)

    assert g.is_win() is False
    assert g.is_loss() is False
    assert g.get_occupied() == [3, 4, 5]

    print()
    g.print_state()


def test_win():
    g = owl.Game(3)

    g.move_owl(3, owl.NEST)
    g.move_owl(4, owl.NEST)
    assert g.is_win() is False

    g.move_owl(5, owl.NEST)
    assert g.is_win() is True


def test_loss():
    g = owl.Game(3)

    for i in range(12):
        g.add_sun()
    assert g.is_loss() is False

    g.add_sun()
    assert g.is_loss() is True


def test_color_query():
    g = owl.Game(3)

    assert g.color_at(0) == owl.Color.yellow
    assert g.color_at(38) == owl.Color.purple


def test_move():
    g = owl.Game(3)
    g.move_owl(3, 7)

    print()
    g.print_state()


def test_compute_end_no_obstacles():
    g = owl.Game(3)
    assert g.compute_end(5, owl.Color.blue) == 6
    assert g.compute_end(5, owl.Color.green) == 10


def test_compute_end_occupied():
    g = owl.Game(3)
    assert g.compute_end(3, owl.Color.purple) == 7
    assert g.compute_end(3, owl.Color.red) == 8


def test_compute_end_nest():
    g = owl.Game(3)
    assert g.compute_end(38, owl.Color.purple) == owl.NEST
    assert g.compute_end(38, owl.Color.red) == owl.NEST
