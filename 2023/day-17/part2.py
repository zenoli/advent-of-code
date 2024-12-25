from typing import Mapping
from heapq import heappop, heappush
import numpy as np


Position = tuple[int, int]
Direction = Position

UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)

directions: Mapping[Direction, int] = {UP: 0, DOWN: 1, LEFT: 2, RIGHT: 3}


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def sub(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] - b[0], a[1] - b[1]


def rot_right(direction):
    x, y = direction
    return y, -x


def rot_left(direction):
    x, y = direction
    return -y, x


def read_input(filename):
    with open(filename) as file:
        lines = [list(map(int, line.strip())) for line in file]
    return np.array(lines)


def on_grid(pos, N, M):
    return pos[0] in range(N) and pos[1] in range(M)


def get_neighbors(pos, d, c, N, M):
    neighbors = []
    if c < 4:
        neighbors = [(add(pos, d), d, c + 1)]

    if c >= 4 and c <= 10:
        neighbors = [
            (add(pos, new_d), new_d, 1) for new_d in [rot_right(d), rot_left(d)]
        ]
    if c < 10:
        neighbors.append((add(pos, d), d, c + 1))

    neighbors = [n for n in neighbors if on_grid(n[0], N, M)]
    return neighbors


def main():
    # grid = read_input("sample.txt")
    # grid = read_input("sample2.txt")
    grid = read_input("input.txt")
    distances = np.full((*grid.shape, 4, 11), np.iinfo(np.int32).max)
    visited = np.full((*grid.shape, 4, 11), False)

    distances[0, 0, :, :] = 0

    N, M = grid.shape

    queue = []
    heappush(queue, (0, ((0, 0), RIGHT, 0)))  # noqa: F821
    heappush(queue, (0, ((0, 0), DOWN, 0)))  # noqa: F821

    while queue:
        min_dist, (pos, d, c) = heappop(queue)

        pos_index = (*pos, directions[d], c)
        if visited[pos_index]:
            continue
        visited[pos_index] = True

        for new_pos, new_d, new_c in get_neighbors(pos, d, c, N, M):
            new_pos_index = (*new_pos, directions[new_d], new_c)
            new_dist = min_dist + grid[new_pos]
            distances[new_pos_index] = min(distances[new_pos_index], new_dist)
            if not visited[new_pos_index]:
                heappush(queue, (distances[new_pos_index], (new_pos, new_d, new_c)))

    print(distances[-1, -1, :, 4:11].min())


if __name__ == "__main__":
    main()

