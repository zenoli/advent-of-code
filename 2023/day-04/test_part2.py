from part2 import get_matches


def test_get_matching_numbers():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    matches = get_matches(line)
    assert matches == 4



