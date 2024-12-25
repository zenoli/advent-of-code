from part1 import compare_hands


def test_compare_hands():
    assert compare_hands("K0K0K", "K0K1K") > 0 
    assert compare_hands("K0K1K", "K0K0K") < 0 
    assert compare_hands("0KK0K", "K0K0K") < 0 
