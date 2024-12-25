import itertools
import re
import bisect
from functools import reduce
from itertools import chain


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


def get_relevant_partition(src_interval, intervals):
    src_start = src_interval[0]
    src_end = sum(src_interval)
    o_id_start, o_id_end = (
        bisect.bisect_right(intervals, src_start),
        bisect.bisect_right(intervals, src_end),
    )
    return [src_start] + intervals[o_id_start:o_id_end] + [src_end]


def compute_dst_intervals_from_partitions(partition, intervals, offsets):
    unmapped_intervals = list(zip(partition, partition[1:]))
    return [
        (map_to_dest(start, intervals, offsets), end - start)
        for start, end in unmapped_intervals
    ]


def map_interval_to_dest(src_interval, map_list):
    intervals, offsets = compute_intervals_and_offsets(map_list)
    partition = get_relevant_partition(src_interval, intervals)
    return compute_dst_intervals_from_partitions(partition, intervals, offsets)


def map_intervals_to_dest(src_intervals, map_list):
    return list(
        itertools.chain(
            *[
                map_interval_to_dest(src_interval, map_list)
                for src_interval in src_intervals
            ]
        )
    )


def map_seed_intervals_to_location_intervals(seed_intervals, map_lists):
    return reduce(map_intervals_to_dest, map_lists, seed_intervals)


def map_to_dest(id, intervals, offsets):
    return id + offsets[bisect.bisect_right(intervals, id)]


def get_seeds_from_ranges(seed_ranges):
    return chain(
        *(
            range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1])
            for i in range(0, len(seed_ranges), 2)
        )
    )


def solve(lines):
    seed_ranges = parse_numbers(lines[0])
    seed_intervals = [
        (seed_ranges[i], seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)
    ]
    map_lists = list(map_list_generator(lines[2:]))

    location_invervals = map_seed_intervals_to_location_intervals(
        seed_intervals, map_lists
    )
    return min((location_interval[0] for location_interval in location_invervals))


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    print(solve(lines))


if __name__ == "__main__":
    main()
