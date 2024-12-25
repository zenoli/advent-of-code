from typing import Mapping
from functools import reduce
from itertools import pairwise
import numpy as np
from skimage.morphology import flood


Position = tuple[int, int]
Direction = Position

UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)

directions: Mapping[str, Direction] = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


def mul(a: tuple[int, ...], factor: int) -> tuple[int, ...]:
    return tuple(map(lambda x: x * factor, a))


def sub(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return add(a, mul(b, -1))


def read_input(filename):
    def parse(line):
        dir, steps, color = line.split()
        return directions[dir], int(steps), color[1:-1]

    with open(filename) as file:
        return list(map(parse, file))


def get_coords(instructions):
    def coord_reducer(coords, instruction):
        dir, steps, _ = instruction
        return coords + [add(coords[-1], mul(dir, steps))]

    return reduce(coord_reducer, instructions, [(0, 0)])


def shift_coords(coords):
    res = np.array(coords)
    return res - np.min(res, axis=0)


def draw(coords):
    grid = np.full(np.max(coords, axis=0) + 1, 0)
    for (x1, y1), (x2, y2) in pairwise(coords):
        grid[min(x1, x2) : max(x1, x2) + 1, min(y1, y2) : max(y1, y2) + 1] = 1
    return grid


def find_interior_point(grid):
    return 1, np.nonzero(grid[1])[0][0] + 1


def fill_pit(grid):
    interior_point = find_interior_point(grid)
    mask = flood(grid, interior_point)
    grid[mask] = 2


def main():
    # instructions = read_input("sample1.txt")
    instructions = read_input("input.txt")

    coords = get_coords(instructions)
    coords = shift_coords(coords)
    grid = draw(coords)
    fill_pit(grid)
    # print(np.count_nonzero(grid))
    np.count_nonzero(grid, axis=0)
    np.savetxt(
        "out/col_counts_correct.txt",
        np.count_nonzero(grid, axis=0),
        fmt="%s",
        delimiter=",",
    )


if __name__ == "__main__":
    main()
