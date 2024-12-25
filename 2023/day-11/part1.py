import numpy as np
from itertools import combinations


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def debug(universe):
    universe_pretty = np.empty_like(universe)
    universe_pretty = np.full(universe.shape, " ")
    universe_pretty[universe] = "#"
    universe_pretty[universe == False] = "."
    print(universe_pretty)


def expand(universe_raw):
    def empty_rows(universe):
        return [i for i, row in enumerate(universe) if not any(row)]

    def empty_cols(universe):
        return [i for i, row in enumerate(universe.T) if not any(row)]

    universe = np.insert(universe_raw, empty_cols(universe_raw), False, axis=1)
    return np.insert(universe, empty_rows(universe_raw), False, axis=0)


def galaxies(universe):
    return zip(*np.where(universe))


def manhattan_distance(a, b):
    return sum(abs(x1 - x2) for x1, x2 in zip(a, b))


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")

    universe_raw = np.array(list(map(list, lines))) == "#"
    universe = expand(universe_raw)

    result = sum(
        manhattan_distance(g1, g2) for g1, g2 in combinations(galaxies(universe), 2)
    )
    print(result)


if __name__ == "__main__":
    main()
