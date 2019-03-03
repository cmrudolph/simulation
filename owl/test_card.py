from owl import Card, Color


def test_card_sun():
    c = Card.create_sun()
    assert c.sun is True
    assert c.color is None


def test_card_colored():
    c = Card.create_colored(Color.green)
    assert c.sun is False
    assert c.color is Color.green
