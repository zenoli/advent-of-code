import numpy as np
from heapq import heappop, heappush


Position = tuple[int, int]
Direction = Position

UP: Direction = (-1, 0)
DOWN: Direction = (1, 0)
LEFT: Direction = (0, -1)
RIGHT: Direction = (0, 1)


def read_input(filename):
    with open(filename) as file:
        lines = [list(line.strip()) for line in file]
    return np.array(lines)


class Part1:
    def __init__(self, input, steps) -> None:
        self.steps = steps
        self.grid = read_input(input)
        self.shortest_paths = np.full(self.grid.shape, self.grid.size)
        self.visited = np.full(self.grid.shape, False)

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

    def get_start(self):
        return tuple(np.argwhere(self.grid == "S")[0])

    def dijkstra(self):
        queue = []
        start = self.get_start()

        self.shortest_paths[start] = 0
        heappush(queue, (self.shortest_paths[start], start))
        while queue:
            _, pos = heappop(queue)
            if self.visited[pos]:
                continue
            self.visited[pos] = True

            for neighbor in self.get_neighbors(pos):
                self.shortest_paths[neighbor] = min(
                    self.shortest_paths[pos] + 1, self.shortest_paths[neighbor]
                )
                if not self.visited[neighbor]:
                    heappush(queue, (self.shortest_paths[neighbor], neighbor))

    def solve(self):
        self.dijkstra()

        return np.count_nonzero(
            (self.shortest_paths <= self.steps) * (self.shortest_paths % 2 == 0)
        )


def main():
    # res = Part1("sample.txt", 6).solve()
    res = Part1("input.txt", 64).solve()

    print(res)


if __name__ == "__main__":
    main()
