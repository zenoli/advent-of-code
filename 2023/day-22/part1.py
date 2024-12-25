from collections import defaultdict
from collections.abc import Iterable
from functools import reduce
from itertools import chain
import numpy as np


type Coord = tuple[int, int, int]
type Brick = tuple[Coord, Coord]


class BrickTower:
    def __init__(self, bricks: Iterable[Brick]) -> None:
        self.bricks = sort_bricks(bricks)
        shape = get_tower_shape(self.bricks)
        self.tower = np.full(shape, None)
        self.top = np.zeros(shape[:2]).astype(int)
        self.settled_heights = dict()

    def drop(self, brick: Brick):
        (x1, y1, z1), (x2, y2, z2) = brick
        brick_height = max(z1, z2) - min(z1, z2) + 1
        z = np.max(
            self.top[min(x1, x2) : max(x1, x2) + 1, min(y1, y2) : max(y1, y2) + 1]
        )
        self.top[min(x1, x2) : max(x1, x2) + 1, min(y1, y2) : max(y1, y2) + 1] = (
            z + brick_height
        )
        self.tower[
            min(x1, x2) : max(x1, x2) + 1,
            min(y1, y2) : max(y1, y2) + 1,
            z + 1 : z + brick_height + 1,
        ] = str(brick)

        self.settled_heights[brick] = z

    def drop_all(self):
        for brick in self.bricks:
            self.drop(brick)

    def compute_supporting_bricks(self):
        supporting_bricks = defaultdict(set)
        for brick in self.bricks:
            (x1, y1, _), (x2, y2, _) = brick
            z = self.settled_heights[brick]
            for supporting_brick in self.tower[
                min(x1, x2) : max(x1, x2) + 1,
                min(y1, y2) : max(y1, y2) + 1,
                z
            ].flatten():  # fmt: off
                if supporting_brick is not None:
                    supporting_bricks[str(brick)].add(supporting_brick)

        return supporting_bricks

    def get_top(self):
        return self.top

    def get_tower(self):
        return self.tower


def read_input(filename: str) -> Iterable[Brick]:
    def parse_line(line: str) -> Brick:
        return tuple(tuple(map(int, s.split(","))) for s in line.split("~"))  # type: ignore

    with open(filename) as file:
        lines = [line.strip() for line in file]
    return map(parse_line, lines)


def sort_bricks(bricks: Iterable[Brick]):
    def key_fn(brick: Brick) -> int:
        return min(c[2] for c in brick)

    return sorted(bricks, key=key_fn)


def get_tower_shape(bricks: Iterable[Brick]) -> Coord:
    return tuple(map(lambda x: x + 1, map(max, zip(*chain(*bricks)))))  # type: ignore


def solve(input):
    bricks = list(read_input(input))

    brick_tower = BrickTower(bricks)
    brick_tower.drop_all()

    unsave_bricks = set.union(
        *(
            supports
            for supports in brick_tower.compute_supporting_bricks().values()
            if len(supports) == 1
        )
    )

    return len(bricks) - len(unsave_bricks)


def main():
    # res = solve("sample.txt")
    res = solve("input.txt")
    print(res)


if __name__ == "__main__":
    main()
