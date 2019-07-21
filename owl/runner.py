#!/usr/bin/env python3

import functools
import multiprocessing as mp
import owl
import strategies
import sys
import uuid


def play(n, owls, players, select, i):
    d = owl.Deck()
    return owl.play(owls, players, d.draw, select)


def run_func(func, write, runs, parallel):
    if parallel:
        with mp.Pool() as p:
            results = p.map(func, range(runs))
    else:
        results = map(func, range(runs))

    for r in results:
        write(f"{r.strategy},{r.players},{r.owls},{r.actions},{r.suns}," +
              f"{1 if r.won else 0},{r.elapsed}")


def write_strategies(write):
    all_strategies = [s for s in dir(strategies) if not s.startswith("__")]
    for s in all_strategies:
        cleaned = [x.title() for x in s.split("_")]
        write(f"{s} | {' '.join(cleaned)}")


def run(runs, write, parallel):
    all_strategies = [s for s in dir(strategies) if not s.startswith("__")]
    for s in all_strategies:
        strategy = getattr(strategies, s)
        for p in [2, 3, 4]:
            for o in [3, 4, 5, 6]:
                func = functools.partial(play, runs, o, p, strategy)
                run_func(func, write, runs, parallel)
                print(f"Done -- R:{runs}; S:{s}; P:{p}; O:{o}")


if __name__ == "__main__":
    runs = int(sys.argv[1])

    strategy_file = "strategies.txt"
    with open(strategy_file, "w") as f:
        write_strategies(lambda x: f.write(x + "\n"))

    result_file = "results.txt"
    with open(result_file, "w") as f:
        run(runs, lambda x: f.write(x + "\n"), parallel=True)
