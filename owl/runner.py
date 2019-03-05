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
              f"{1 if r.won else 0},1,{r.elapsed}")


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
    file_name = "results.txt"
    with open(file_name, "w") as f:
        f.write("Strategy,Players,Owls,Actions,Suns,Won,Played,Elapsed\n")
        run(runs, lambda x: f.write(x + "\n"), parallel=True)
