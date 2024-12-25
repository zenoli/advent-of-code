from part1 import DOWN, RIGHT, add, get_coords, mul, sub


def test_tuple_arithmetic():
    assert add((0, 1), (1, 0)) == (1, 1)
    assert sub((1, 1), (1, 0)) == (0, 1)
    assert mul((1, -2), -1) == (-1, 2)


def test_get_coords():
    instructions = [(DOWN, 6, ""), (RIGHT, 3, "")]
    coords = get_coords(instructions)
    assert coords == [(0, 0), (6, 0), (6, 3)]
