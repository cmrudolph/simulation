#!/usr/bin/env python3

# Simulation of the children's game "Hoot Owl Hoot". The game involves simple
# decision making, which provides an opportunity to simulate and compare
# strategies.

import attr
import pprint
import random
from enum import Enum

NEST = 888

ORIG_BOARD = "YGOBP RBPRY GBORP YGOBP RGYOB PRYGB ORPYG BORP"

BOARD_SPACES = (
    [6, 2, 3, 1, 4, 5, 1, 4, 5, 6,
     2, 1, 3, 5, 4, 6, 2, 3, 1, 4,
     5, 2, 6, 3, 1, 4, 5, 6, 2, 1,
     3, 5, 4, 6, 2, 1, 3, 5, 4]
)


class Color(Enum):
    blue = 1
    green = 2
    orange = 3
    purple = 4
    red = 5
    yellow = 6


@attr.s(frozen=True)
class Card(object):
    sun = attr.ib()
    color = attr.ib()

    @classmethod
    def create_sun(cls):
        return cls(True, None)

    @classmethod
    def create_colored(cls, color):
        return cls(False, color)


@attr.s
class Hand(object):
    cards = attr.ib(init=False, factory=list)

    def add(self, card):
        self.cards.append(card)

    def find_sun(self):
        return next((c for c in self.cards if c.sun), None)

    def remove(self, card):
        self.cards.remove(card)


@attr.s
class Deck(object):
    _cards = attr.ib(init=False)

    @_cards.default
    def _init_cards(self):
        result = []
        result.extend([Card.create_sun()] * 14)
        for color in Color:
            result.extend([Card.create_colored(color)] * 6)
        random.shuffle(result)

        return result

    def draw(self):
        return self._cards.pop()


@attr.s
class Space(object):
    index = attr.ib()
    color = attr.ib()
    owl = attr.ib(init=False, default=None)


@attr.s
class Game(object):
    owls = attr.ib()
    _spaces = attr.ib(init=False)
    starting_owls = attr.ib(init=False)
    suns = attr.ib(init=False, default=0)
    actions = attr.ib(init=False, default=0)

    @_spaces.default
    def _init_spaces(self):
        result = []
        for i, bs in enumerate(BOARD_SPACES):
            result.append(Space(i, Color(bs)))

        for i in range(self.owls):
            owl_num = i + 1
            result[5-i].owl = owl_num

        return result

    @starting_owls.default
    def _init_starting_owls(self):
        return self.owls

    def is_win(self):
        return self.owls == 0

    def is_loss(self):
        return self.suns == 13

    def add_sun(self):
        self.actions += 1
        self.suns += 1

    def get_occupied(self):
        return [i for i, v in enumerate(self._spaces) if v.owl is not None]

    def _can_move_to(self, idx, color):
        color_match = self._spaces[idx].color == color
        is_open = self._spaces[idx].owl is None

        return color_match and is_open

    def compute_end(self, start, color):
        end = start + 1
        while end < len(self._spaces) and not self._can_move_to(end, color):
            end += 1

        return NEST if end == len(self._spaces) else end

    def print_header(self):
        for i in range(len(self._spaces)):
            if i > 0 and i % 5 == 0:
                print("|", end="")
            print(self._spaces[i].color.name[0], end="")
        print()

    def print_stats(self):
        print(f"Won:{self.is_win()}; Loss:{self.is_loss()}; " +
              f"Act:{self.actions}; Sun:{self.suns}; Owls:{self.owls}")

    def print_state(self):
        for i in range(len(self._spaces)):
            if i > 0 and i % 5 == 0:
                print("|", end="")
            owl = self._spaces[i].owl
            owl_str = " " if owl is None else owl
            print(owl_str, end="")
        print(f" -- N({self.starting_owls - self.owls}) -- S({self.suns})")

    def move_owl(self, start, end):
        assert start >= 0, "Start too small"
        assert start < len(self._spaces), "Start too big"
        assert end < len(self._spaces) or end == NEST, "End too big"
        assert end > start, "End  before start"
        assert self._spaces[start].owl is not None, "Start not occupied"
        assert end == NEST or self._spaces[end].owl is None, "End occupied"

        if end == NEST:
            self.owls -= 1
        else:
            self._spaces[end].owl = self._spaces[start].owl
        self._spaces[start].owl = None
        self.actions += 1

    def color_at(self, idx):
        return self._spaces[idx].color


def play(owls, players, draw, select):
    game = Game(owls)
    hands = []
    for p in range(players):
        hand = Hand()
        hand.add(draw())
        hand.add(draw())
        hand.add(draw())
        hands.append(hand)

    hand_idx = 0
    game.print_header()
    while not (game.is_win() or game.is_loss()):
        hand = hands[hand_idx]
        sun = hand.find_sun()

        if sun is not None:
            game.add_sun()
            hand.remove(sun)
        else:
            owl, card = select(game, hands, hand_idx)
            hand.remove(card)

            end = game.compute_end(owl, card.color)
            game.move_owl(owl, end)

        drawn = draw()
        if drawn is not None:
            hand.add(drawn)

        hand_idx += 1
        if hand_idx == len(hands):
            hand_idx = 0

        game.print_state();
    game.print_stats()


def first_owl_first_card(game, hands, hand_idx):
    return (game.get_occupied()[0], hands[hand_idx].cards[0])
