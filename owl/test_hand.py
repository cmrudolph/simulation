import owl

red = owl.Card.create_colored(owl.Color.red)
green = owl.Card.create_colored(owl.Color.green)
sun = owl.Card.create_sun()


def test_hand_empty():
    h = owl.Hand()
    assert h.cards == []
    assert h.find_sun() is None


def test_hand_has_sun():
    h = owl.Hand()
    h.add(green)
    h.add(sun)
    assert h.cards == [green, sun]
    assert h.find_sun() is sun


def test_hand_no_sun():
    h = owl.Hand()
    h.add(green)
    h.add(red)
    assert h.cards == [green, red]
    assert h.find_sun() is None


def test_hand_removing():
    h = owl.Hand()
    h.add(green)
    h.add(red)
    assert h.cards == [green, red]

    h.remove(red)
    assert h.cards == [green]

    h.remove(green)
    assert h.cards == []
