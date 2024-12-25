from part1 import get_numbers, compute_score, read_input, solve


def test_borders_symbol():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    winning, ours = get_numbers(line)

    assert winning == {41, 48, 83, 86, 17}
    assert ours == {83, 86, 6, 31, 17, 9, 48, 53}


def test_compute_score():
    assert compute_score({1}, {1}) == 1
    assert compute_score(set(), {1}) == 0
    assert compute_score({1}, set()) == 0
    assert compute_score({1, 2, 3}, {1, 2, 3}) == 4


