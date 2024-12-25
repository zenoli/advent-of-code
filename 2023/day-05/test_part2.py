from part2 import (
    compute_dst_intervals_from_partitions,
    compute_intervals_and_offsets,
    get_seeds_from_ranges,
    map_interval_to_dest,
    map_intervals_to_dest,
    map_seed_intervals_to_location_intervals,
)


def test_get_seeds_from_ranges():
    seeds = list(get_seeds_from_ranges([1, 3, 5, 2]))
    assert seeds == [1, 2, 3, 5, 6]


def test_get_compute_intervals_from_partitions():
    partitions = [15, 20, 30, 40, 45]
    intervals = [10, 20, 30, 40, 50]
    offsets = [0, 2, -5, 22, 13, 0]

    res = compute_dst_intervals_from_partitions(partitions, intervals, offsets)
    assert res == [(17, 5), (15, 10), (52, 10), (53, 5)]


def test_compute_intervals_and_offsets():
    map_list = [
        [12, 10, 10],
        [15, 20, 10],
        [52, 30, 10],
        [53, 40, 10],

    ]  # fmt: off

    intervals, offsets = compute_intervals_and_offsets(map_list)
    assert intervals == [10, 20, 30, 40, 50]
    assert offsets == [0, 2, -5, 22, 13, 0]


def test_map_interval_to_dest():
    src_interval = [15, 30]
    map_list = [
        [12, 10, 10],
        [15, 20, 10],
        [52, 30, 10],
        [53, 40, 10],

    ]  # fmt: off

    dst_intervals = map_interval_to_dest(src_interval, map_list)
    assert dst_intervals == [(17, 5), (15, 10), (52, 10), (53, 5)]


def test_map_intervals_to_dest():
    src_interval = (15, 30)
    map_list = [
        [12, 10, 10],
        [15, 20, 10],
        [52, 30, 10],
        [53, 40, 10],

    ]  # fmt: off

    dst_intervals = map_intervals_to_dest([src_interval], map_list)
    assert dst_intervals == [(17, 5), (15, 10), (52, 10), (53, 5)]

