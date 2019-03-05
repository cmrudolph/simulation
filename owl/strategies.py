def back_owl_random_card(game, hands, hand_idx, randint):
    hand = hands[hand_idx]
    card_idx = randint(0, 2)
    return (game.occupied[0], hand.cards[card_idx])


def random_owl_random_card(game, hands, hand_idx, randint):
    hand = hands[hand_idx]
    owl_idx = randint(0, game.owls - 1)
    card_idx = randint(0, len(hand.cards) - 1)
    return (game.occupied[owl_idx], hand.cards[card_idx])


def front_owl_random_card(game, hands, hand_idx, randint):
    hand = hands[hand_idx]
    card_idx = randint(0, 2)
    return (game.occupied[-1], hand.cards[card_idx])


def back_owl_smallest_gain(game, hands, hand_idx, randint):
    worst_gain = 888
    start = game.occupied[0]
    for card in hands[hand_idx].cards:
        end = game.compute_end(start, card.color)
        gain = end - start
        if gain < worst_gain:
            worst_gain = gain
            worst_card = card

    return (start, worst_card)


def any_owl_smallest_gain(game, hands, hand_idx, randint):
    worst_gain = 888
    for start in game.occupied:
        for card in hands[hand_idx].cards:
            end = game.compute_end(start, card.color)
            gain = end - start
            if gain < worst_gain:
                worst_gain = gain
                worst_start = start
                worst_card = card

    return (worst_start, worst_card)


def front_owl_smallest_gain(game, hands, hand_idx, randint):
    worst_gain = 888
    start = game.occupied[-1]
    for card in hands[hand_idx].cards:
        end = game.compute_end(start, card.color)
        gain = end - start
        if gain < worst_gain:
            worst_gain = gain
            worst_card = card

    return (start, worst_card)


def back_owl_biggest_gain(game, hands, hand_idx, randint):
    best_gain = 0
    start = game.occupied[0]
    for card in hands[hand_idx].cards:
        end = game.compute_end(start, card.color)
        gain = end - start
        if gain > best_gain:
            best_gain = gain
            best_card = card

    return (start, best_card)


def any_owl_biggest_gain(game, hands, hand_idx, randint):
    best_gain = 0
    for start in game.occupied:
        for card in hands[hand_idx].cards:
            end = game.compute_end(start, card.color)
            gain = end - start
            if gain > best_gain:
                best_gain = gain
                best_start = start
                best_card = card

    return (best_start, best_card)


def front_owl_biggest_gain(game, hands, hand_idx, randint):
    best_gain = 0
    start = game.occupied[-1]
    for card in hands[hand_idx].cards:
        end = game.compute_end(start, card.color)
        gain = end - start
        if gain > best_gain:
            best_gain = gain
            best_card = card

    return (start, best_card)


def back_owl_color_priority(game, hands, hand_idx, randint):
    min_card = 888
    start = game.occupied[0]
    for card in hands[hand_idx].cards:
        if card.color.value < min_card:
            min_card = card.color.value
            best_card = card

    return (start, best_card)


def front_owl_color_priority(game, hands, hand_idx, randint):
    min_card = 888
    start = game.occupied[-1]
    for card in hands[hand_idx].cards:
        if card.color.value < min_card:
            min_card = card.color.value
            best_card = card

    return (start, best_card)
