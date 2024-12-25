from typing import Mapping
from functools import reduce
from itertools import pairwise
from collections import defaultdict
import numpy as np
import math


Position = tuple[int, int]
Direction = Position

UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)

directions: Mapping[str, Direction] = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}
directions_hex: Mapping[str, Direction] = {"3": UP, "1": DOWN, "2": LEFT, "0": RIGHT}


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


def mul(a: tuple[int, ...], factor: int) -> tuple[int, ...]:
    return tuple(map(lambda x: x * factor, a))


def closed(r):
    return range(r[0], r[-1] + 2)


def read_input(filename):
    def parse(line):
        dir, steps, _ = line.split()
        return directions[dir], int(steps)

    def parse_hex(line):
        _, _, color = line.split()
        return directions_hex[color[-2]], int(color[2:7], 16)

    with open(filename) as file:
        return list(map(parse_hex, file))


def get_coords(instructions):
    def coord_reducer(coords, instruction):
        dir, steps = instruction
        return coords + [add(coords[-1], mul(dir, steps))]

    return reduce(coord_reducer, instructions, [(0, 0)])


def shift_coords(coords):
    res = np.array(coords)
    return res - np.min(res, axis=0)


def draw(coords):
    grid = np.full(np.max(coords, axis=0) + 1, ".")
    for (x1, y1), (x2, y2) in pairwise(coords):
        grid[min(x1, x2) : max(x1, x2) + 1, min(y1, y2) : max(y1, y2) + 1] = "#"
    return grid


def scan_points_generator(coords):
    scan_points = sorted(set(map(int, coords[:, 1])))
    for p1, p2 in pairwise(scan_points):
        yield p1
        if p1 + 1 < p2:
            yield p1 + 1
    yield scan_points[-1]
    yield scan_points[-1] + 1


def get_horizontal_lines(coords):
    d = defaultdict(list)
    intervals = (
        (x, closed(range(min(y1, y2), max(y1, y2))))
        for (x, y1), (_, y2) in pairwise(coords)
        if y1 != y2
    )

    for x, interval in intervals:
        d[x].append(interval)
    return dict(sorted(d.items()))


def get_intervals(point, intervals):
    def get_range(point, ranges):
        for r in ranges:
            if point in r:
                return r
        return None

    return (
        (x, r) for x, ranges in intervals.items() if (r := get_range(point, ranges))
    )


def calculate_slice(point, horizontal_lines):
    def reset():
        return None, (math.inf, -math.inf)

    slice = 0
    start = None
    opening_interval, closing_interval = reset()
    for x, r in get_intervals(point, horizontal_lines):
        r_start, r_end = r[0], r[-1]
        if opening_interval is None:
            opening_interval = (r_start, r_end)
            start = x
            continue

        # Case: <-->
        if opening_interval[0] < point and point < opening_interval[1]:
            closing_interval = (
                min(r_start, closing_interval[0]),
                max(r_end, closing_interval[1]),
            )

            if closing_interval[0] < point and point < closing_interval[1]:
                slice += (x - start) + 1
                opening_interval, closing_interval = reset()
            continue

        if (
            point == opening_interval[0]
            and point == r_end
            or point == opening_interval[1]
            and point == r_start
        ):
            opening_interval = (
                min(r_start, opening_interval[0]),
                max(r_end, opening_interval[1]),
            )
            continue
        # Case: { <--, -->}
        if (
            point == opening_interval[0]
            and point == r_start
            or point == opening_interval[1]
            and point == r_end
            or r_start < point
            and point < r_end
        ):
            slice += (x - start) + 1
            opening_interval, closing_interval = reset()

    return slice


def calculate_pit_size(scan_points, horizontal_lines):
    def calculate_block(interval):
        start, end = interval
        slice_size = calculate_slice(start, horizontal_lines)
        return slice_size * (end - start)

    return sum(map(calculate_block, pairwise(scan_points)))


def main():
    # instructions = read_input("sample1.txt")
    instructions = read_input("input.txt")

    coords = get_coords(instructions)
    coords = shift_coords(coords)
    scan_points = scan_points_generator(coords)
    horizontal_lines = get_horizontal_lines(coords)

    pit_size = calculate_pit_size(scan_points, horizontal_lines)
    print(pit_size)


if __name__ == "__main__":
    main()
