import numpy as np
from itertools import combinations


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]

    return list(map(parse, lines))


def parse(line):
    def to_tuple(s):
        return np.array(list(map(int, s.split(","))))[:2]

    return tuple(map(to_tuple, line.split("@")))


def intersection(p1, v1, p2, v2):
    V = np.column_stack([v1, -v2])
    p = p2 - p1
    try:
        t = np.linalg.solve(V, p)
        if all(t >= 0):
            return p1 + t[0] * v1
    except Exception as _:
        return None


def solve(input, lower_bound, upper_bound):
    hailstones = read_input(input)
    return sum(
        (
            (i := intersection(p1, v1, p2, v2)) is not None
            and all(i >= lower_bound)
            and all(i <= upper_bound)
        )
        for (p1, v1), (p2, v2) in combinations(hailstones, r=2)
    )


def main():
    # lower_bound = 7
    # upper_bound = 27
    # res = solve("sample.txt", lower_bound, upper_bound)
    lower_bound = 200000000000000
    upper_bound = 400000000000000
    res = solve("input.txt", lower_bound, upper_bound)
    print(res)


if __name__ == "__main__":
    main()
