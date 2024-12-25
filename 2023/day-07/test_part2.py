from part2 import (
    get_strength,
    FIVE_OF_A_KIND,
    FOUR_OF_A_KIND,
    FULL_HOUSE,
)


def test_get_strength():
    assert get_strength("K0K0J") == FULL_HOUSE
    assert get_strength("K0KJJ") == FOUR_OF_A_KIND
    assert get_strength("KKKKK") == FIVE_OF_A_KIND
    assert get_strength("JJJJJ") == FIVE_OF_A_KIND
