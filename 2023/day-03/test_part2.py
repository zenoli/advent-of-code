from part2 import get_surrounding_gears


def test_borders_symbol():
    S = [
        ".*.",
        "*.*",
        "...",
    ]  # fmt: off

    gears = get_surrounding_gears(1, 1, S)

    assert (0, 1) in gears
    assert (1, 0) in gears
    assert (1, 2) in gears
    assert len(gears) == 3

