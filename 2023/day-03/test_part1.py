from part1 import borders_symbol


def test_borders_symbol():
    S = [
        "....",
        "..x.",
        "....",
        "....",
    ]  # fmt: off
    assert borders_symbol(0, 0, S) is False
    assert borders_symbol(0, 1, S) is True
    assert borders_symbol(0, 2, S) is True
    assert borders_symbol(0, 3, S) is True

    assert borders_symbol(1, 0, S) is False
    assert borders_symbol(1, 1, S) is True
    assert borders_symbol(1, 2, S) is True
    assert borders_symbol(1, 3, S) is True

    assert borders_symbol(2, 0, S) is False
    assert borders_symbol(2, 1, S) is True
    assert borders_symbol(2, 2, S) is True
    assert borders_symbol(2, 3, S) is True

    assert borders_symbol(3, 0, S) is False
    assert borders_symbol(3, 1, S) is False
    assert borders_symbol(3, 2, S) is False
    assert borders_symbol(3, 3, S) is False
