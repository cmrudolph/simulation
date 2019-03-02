#!/usr/bin/env python3

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
    cards = attr.ib(factory=list)

    def add(self, card):
        self.cards.append(card)

    def find_sun(self):
        return next((c for c in self.cards if c.sun), None)

    def remove(self, card):
        self.cards.remove(card)


class Deck(object):
    def __init__(self):
        self._cards = []
        self._cards.extend([Card.create_sun()] * 14)
        for color in Color:
            self._cards.extend([Card.create_colored(color)] * 6)
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


@attr.s
class Space(object):
    index = attr.ib()
    color = attr.ib()
    owl = attr.ib(default=None)


class Board(object):
    def __init__(self, owls):
        self._spaces = []
        self.owls = owls
        self.suns = 0
        self.actions = 0

        for i, bs in enumerate(BOARD_SPACES):
            self._spaces.append(Space(i, Color(bs)))

        for i in range(owls):
            owl_num = i + 1
            self._spaces[5-i].owl = owl_num

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

    def print_state(self):
        print(f"Act:{self.actions} | Sun:{self.suns} | Owls:{self.owls}")
        for i in range(len(self._spaces)):
            if i > 0 and i % 5 == 0:
                print("|", end="")
            print(self._spaces[i].color.name[0], end="")
        print()

        for i in range(len(self._spaces)):
            if i > 0 and i % 5 == 0:
                print("|", end="")
            owl = self._spaces[i].owl
            owl_str = " " if owl is None else owl
            print(owl_str, end="")
        print()

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
