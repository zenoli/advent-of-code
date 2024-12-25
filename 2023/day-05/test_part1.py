from part1 import compute_intervals_and_offsets, map_to_dest


def test_compute_intervals_and_offsets():
    intervals, offsets = compute_intervals_and_offsets([[50, 98, 2], [52, 50, 48]])
    assert intervals == [50, 98, 100]
    assert offsets == [0, 2, -48, 0]

    intervals, offsets = compute_intervals_and_offsets([[0, 15, 37], [37, 52, 2], [39, 0, 15]])
    assert intervals == [0, 15, 52, 54]
    assert offsets == [0, 39, -15, -15, 0]

    intervals, offsets = compute_intervals_and_offsets([[0, 20, 32], [37, 52, 2], [39, 0, 15]])
    assert intervals == [0, 15, 20, 52, 54]
    assert offsets == [0, 39, 0, -20, -15, 0]

def test_map_to_dest():
    intervals = [50, 98, 100]
    offsets = [0, 2, -48, 0]
    assert map_to_dest(79, intervals, offsets) == 81
    assert map_to_dest(14, intervals, offsets) == 14
    assert map_to_dest(55, intervals, offsets) == 57
    assert map_to_dest(13, intervals, offsets) == 13

    assert map_to_dest(13, [0, 15, 20, 52, 54], [0, 39, 0, -20, -15, 0]) == 52
    assert map_to_dest(17, [0, 15, 20, 52, 54], [0, 39, 0, -20, -15, 0]) == 17
