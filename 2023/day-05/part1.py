import re
import bisect
from functools import reduce


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_numbers(line):
    return list(map(int, re.findall(r"\d+", line)))


def map_list_generator(lines):
    mappings = []
    for line in lines:
        if numbers := parse_numbers(line):
            mappings.append(numbers)
        if not line:
            yield mappings
            mappings = []
    yield mappings


def compute_intervals_and_offsets(map_list):
    map_list_sorted = sorted(map_list, key=lambda x: x[1])
    intervals, offsets = [map_list_sorted[0][1]], []
    for dst, src, range in map_list_sorted:
        offset = dst - src
        if intervals[-1] != src:
            intervals.append(src)
            offsets.append(0)

        intervals.append(src + range)
        offsets.append(offset)

    return intervals, [0] + offsets + [0]


def map_to_dest(id, intervals, offsets):
    return id + offsets[bisect.bisect_right(intervals, id)]


def map_seed_to_location(seed, map_lists):
    def f(id, map_list):
        intermediate = map_to_dest(id, *compute_intervals_and_offsets(map_list))
        return intermediate

    return reduce(f, map_lists, seed)


def solve(lines):
    seeds = parse_numbers(lines[0])
    map_lists = list(map_list_generator(lines[2:]))

    return min(map_seed_to_location(seed, map_lists) for seed in seeds)


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    print(solve(lines))


if __name__ == "__main__":
    main()
