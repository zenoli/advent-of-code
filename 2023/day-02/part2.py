from collections.abc import Iterable
from collections import defaultdict
from functools import reduce
import math
from typing import Dict, Tuple

colors = ["red", "green", "blue"]


def power(max_colors: dict[str, int]) -> int:
    return math.prod(max_colors.values())


def read_input(filename: str) -> Iterable[str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def max_reducer(grab1: Dict[str, int], grab2: Dict[str, int]) -> Dict[str, int]:
    return defaultdict(
        int, {color: max(grab1[color], grab2[color]) for color in colors}
    )


def compute_max_colors(grabs: Iterable[Dict[str, int]]) -> Dict[str, int]:
    return reduce(max_reducer, grabs)


def parse_line(line: str) -> Iterable[Dict[str, int]]:
    _, set_string = line.split(": ")
    return map(parse_set_string, set_string.split("; "))


def parse_set_string(set_string: str) -> Dict[str, int]:
    entries = set_string.split(", ")
    return defaultdict(int, map(parse_entry, entries))


def parse_entry(entry: str) -> Tuple[str, int]:
    count, color = entry.split(" ")
    return color, int(count)


def parse_id(id_string: str) -> int:
    return int(id_string.split(" ")[1])


def solve_line(line: str) -> int:
    grabs = parse_line(line)
    return power(compute_max_colors(grabs))


def solve(lines: Iterable[str]) -> int:
    return sum(map(solve_line, lines))


def main():
    lines = read_input("input.txt")
    # lines = read_input("sample-part2.txt")
    print(solve(lines))


if __name__ == "__main__":
    main()
