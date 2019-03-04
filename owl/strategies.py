def back_owl_first_card(game, hands, hand_idx):
    return (game.get_occupied()[0], hands[hand_idx].cards[0])


def back_owl_biggest_gain(game, hands, hand_idx):
    best_gain = 0
    start = game.get_occupied()[0]
    for card in hands[hand_idx].cards:
        end = game.compute_end(start, card.color)
        gain = end - start
        if gain > best_gain:
            best_gain = gain
            best_start = start
            best_card = card

    return (start, best_card)


def any_owl_biggest_gain(game, hands, hand_idx):
    best_gain = 0
    for start in game.get_occupied():
        for card in hands[hand_idx].cards:
            end = game.compute_end(start, card.color)
            gain = end - start
            if gain > best_gain:
                best_gain = gain
                best_start = start
                best_card = card

    return (best_start, best_card)
