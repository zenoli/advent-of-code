from itertools import product


def read_input(filename: str):
    def parse_block(block_str: str) -> list[str]:
        return [line for line in block_str.split("\n")]

    def get_heights(block: list[str]) -> tuple[int, ...]:
        x_size = len(block)
        y_size = len(block[0])
        heights = [-1] * y_size

        for x, y in product(range(x_size), range(y_size)):
            heights[y] += block[x][y] == "#"
        return tuple(heights)

    with open(filename) as file:
        file_str = file.read()

    blocks = file_str.rstrip().split("\n\n")

    locks, keys = [], []

    for block in map(parse_block, blocks):
        heights = get_heights(block)
        if set(block[0]) == {"#"}:
            locks.append(heights)
        else:
            keys.append(heights)
    return locks, keys


def add(t1: tuple[int, ...], t2: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(t1, t2))


def does_fit(key: tuple[int, ...], lock: tuple[int, ...]) -> bool:
    return all(s < 6 for s in add(key, lock))


def main():
    # locks, keys = read_input("sample.txt")
    locks, keys = read_input("input.txt")

    result = sum(does_fit(key, lock) for key, lock in product(keys, locks))
    print(result)


if __name__ == "__main__":
    main()
