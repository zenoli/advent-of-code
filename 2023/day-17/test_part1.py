from part1 import get_neighbors, UP, DOWN, LEFT, RIGHT, add, sub, rot_left, rot_right


def test_get_neighbors():
    neighbors = get_neighbors((1, 1), RIGHT, 2, 3, 3)
    assert set(neighbors) == {
        ((0, 1), UP, 1),
        ((2, 1), DOWN, 1),
        ((1, 2), RIGHT, 3),
    }

    neighbors = get_neighbors((1, 1), RIGHT, 3, 3, 3)
    assert set(neighbors) == {((0, 1), UP, 1), ((2, 1), DOWN, 1)}

    neighbors = get_neighbors((1, 1), RIGHT, 2, 2, 2)
    assert set(neighbors) == {((0, 1), UP, 1)}

    neighbors = get_neighbors((1, 1), DOWN, 1, 3, 3)
    assert set(neighbors) == {((1, 0), LEFT, 1), ((1, 2), RIGHT, 1), ((2, 1), DOWN, 2)}


def test_add():
    assert add((1, 2), (2, 3)) == (3, 5)


def test_sub():
    assert sub((3, 2), (1, 2)) == (2, 0)


def test_rot_right():
    assert rot_right(UP) == RIGHT
    assert rot_right(RIGHT) == DOWN
    assert rot_right(DOWN) == LEFT
    assert rot_right(LEFT) == UP


def test_rot_left():
    assert rot_left(RIGHT) == UP
    assert rot_left(DOWN) == RIGHT
    assert rot_left(LEFT) == DOWN
    assert rot_left(UP) == LEFT
