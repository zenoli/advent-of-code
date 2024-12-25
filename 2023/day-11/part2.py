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


def empty_rows(universe):
    return [i for i, row in enumerate(universe) if not any(row)]


def empty_cols(universe):
    return [i for i, row in enumerate(universe.T) if not any(row)]


def galaxies(universe):
    return zip(*np.where(universe))


def manhattan_distance(a, b):
    return sum(abs(x1 - x2) for x1, x2 in zip(a, b))


def expanded_spaces_to_cross(start, end, spaces):
    return sum(row in range(start, end) for row in spaces)


def expanded_distance(g1, g2, exp_rows, exp_cols, expansion_factor):
    row_start, row_end = min(g1[0], g2[0]), max(g1[0], g2[0])
    col_start, col_end = min(g1[1], g2[1]), max(g1[1], g2[1])

    expanded_row_spaces = expanded_spaces_to_cross(row_start, row_end, exp_rows)
    expanded_col_spaces = expanded_spaces_to_cross(col_start, col_end, exp_cols)
    return (
        manhattan_distance(g1, g2)
        + (expanded_row_spaces + expanded_col_spaces) * (expansion_factor - 1)
    )


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")

    universe = np.array(list(map(list, lines))) == "#"
    rows = empty_rows(universe)
    cols = empty_cols(universe)

    result = sum(
        expanded_distance(g1, g2, rows, cols, 1000000) for g1, g2 in combinations(galaxies(universe), 2)
    )
    print(result)


if __name__ == "__main__":
    main()
