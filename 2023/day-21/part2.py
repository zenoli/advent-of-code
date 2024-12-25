import numpy as np
from heapq import heappop, heappush


type Position = tuple[int, int]
type Direction = Position

UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)


class Dijkstra:
    def __init__(self, grid) -> None:
        self.grid = grid

    def on_grid(self, pos) -> bool:
        return (
            all(map(lambda x: x >= 0, pos))
            and pos[0] < self.grid.shape[0]
            and pos[1] < self.grid.shape[1]
        )

    def get_neighbors(self, pos):
        directions = np.array([UP, DOWN, LEFT, RIGHT])
        neighbors = (tuple(n) for n in pos + directions)
        return (n for n in neighbors if self.on_grid(n) and self.grid[n] != "#")

    def solve(self, start):
        queue = []

        shortest_paths = np.full(self.grid.shape, self.grid.size)
        visited = np.full(self.grid.shape, False)
        shortest_paths[start] = 0
        heappush(queue, (shortest_paths[start], start))
        while queue:
            _, pos = heappop(queue)
            if visited[pos]:
                continue
            visited[pos] = True

            for neighbor in self.get_neighbors(pos):
                shortest_paths[neighbor] = min(
                    int(shortest_paths[pos] + 1),
                    int(shortest_paths[neighbor]),
                )
                if not visited[neighbor]:
                    heappush(queue, (shortest_paths[neighbor], neighbor))
        return shortest_paths


def read_input(filename):
    with open(filename) as file:
        lines = [list(line.strip()) for line in file]
    return np.array(lines)


def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_start(grid):
    return tuple(np.argwhere(grid == "S")[0])


def checkerboard(shape):
    return (np.indices(shape).sum(axis=0) % 2).astype(bool)


def solve(input):
    grid = read_input(input)
    start = get_start(grid)

    shortest_paths = Dijkstra(grid).solve(start)

    odd = checkerboard(grid.shape)
    even = np.invert(odd)

    block = shortest_paths <= 130
    corners = (shortest_paths > 65) & (shortest_paths != grid.size)

    block_odd = np.count_nonzero(block & odd)
    block_even = np.count_nonzero(block & even)

    corners_odd = np.count_nonzero(corners & odd)
    corners_even = np.count_nonzero(corners & even)

    n = (26501365 - 65) // 131
    result = (
        (n + 1) * (n + 1) * block_odd
        - (n + 1) * corners_odd
        + n * n * block_even
        + n * corners_even
    )

    return result


def main():
    print(solve("input.txt"))


if __name__ == "__main__":
    main()
