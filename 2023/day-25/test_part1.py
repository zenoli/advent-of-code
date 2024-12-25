from part1 import Karger, debug


def test_edge_contraction():
    input = {
        1: [2, 3],
        2: [3, 4, 4],
        3: [4]
    }  # fmt: off
    karger = Karger(input)
    karger.contract((1, 2))

    debug(karger.adj)
    assert karger.adj == [
        [0, 2, 0, 0],
        [2, 0, 3, 0],
        [0, 3, 0, 0],
        [0, 0, 0, 0]
    ]  # fmt: off

    assert karger.N == 3
    assert karger.edge_counts == [2, 5, 3, 0]
    assert karger.vertex_merge_counts == [1, 2, 1, 0]


def test_adjacency_matrix_generation():
    input = {
        1: [2, 3],
        2: [3, 4, 4],
        3: [4]
    }  # fmt: off
    karger = Karger(input)

    assert karger.adj == [
        [0, 1, 1, 0],
        [1, 0, 1, 2],
        [1, 1, 0, 1],
        [0, 2, 1, 0]
    ]  # fmt: off


def test_karger():
    input = {
        1: [2, 3],
        2: [3, 4, 4],
        3: [4]
    }  # fmt: off
    karger = Karger(input)
    karger.contract((1, 2))

    assert karger.adj == [
        [0, 2, 0, 0],
        [2, 0, 3, 0],
        [0, 3, 0, 0],
        [0, 0, 0, 0]
    ]  # fmt: off


if __name__ == "__main__":
    test_karger()
