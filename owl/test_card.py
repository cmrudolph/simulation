import owl


def test_card_sun():
    c = owl.Card.create_sun()
    assert c.sun is True
    assert c.color is None


def test_card_colored():
    c = owl.Card.create_colored(owl.Color.green)
    assert c.sun is False
    assert c.color is owl.Color.green
