from part1 import is_cyclic


def test_is_cyclic():
    graph = {"a": [("b", 1)], "b": [("a", 1)]}
    assert is_cyclic(graph) is True

    graph = {"a": [("b", 1), ("c", 1)], "b": [("c", 1)], "c": []}
    assert is_cyclic(graph) is False
