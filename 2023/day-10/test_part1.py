from part1 import move
import numpy as np


def test_move():
    next_pos = move(np.array([1, 1]), np.array([0, 1]), "L")
    assert np.array_equal(next_pos, np.array([1, 2]))

    next_pos = move(np.array([1, 1]), np.array([1, 2]), "L")
    assert np.array_equal(next_pos, np.array([0, 1]))

    next_pos = move(np.array([1, 1]), np.array([1, 2]), "F")
    assert np.array_equal(next_pos, np.array([2, 1]))

    next_pos = move(np.array([1, 1]), np.array([2, 1]), "F")
    assert np.array_equal(next_pos, np.array([1, 2]))

    next_pos = move(np.array([1, 1]), np.array([0, 1]), "J")
    assert np.array_equal(next_pos, np.array([1, 0]))

    next_pos = move(np.array([1, 1]), np.array([1, 0]), "J")
    assert np.array_equal(next_pos, np.array([0, 1]))

    next_pos = move(np.array([1, 1]), np.array([1, 0]), "7")
    assert np.array_equal(next_pos, np.array([2, 1]))

    next_pos = move(np.array([1, 1]), np.array([2, 1]), "7")
    assert np.array_equal(next_pos, np.array([1, 0]))

    next_pos = move(np.array([1, 1]), np.array([0, 1]), "|")
    assert np.array_equal(next_pos, np.array([2, 1]))

    next_pos = move(np.array([1, 1]), np.array([2, 1]), "|")
    assert np.array_equal(next_pos, np.array([0, 1]))

    next_pos = move(np.array([1, 1]), np.array([1, 0]), "-")
    assert np.array_equal(next_pos, np.array([1, 2]))

    next_pos = move(np.array([1, 1]), np.array([1, 2]), "-")
    assert np.array_equal(next_pos, np.array([1, 0]))
