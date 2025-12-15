from itertools import batched


def read_input(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    line = lines[0]
    ranges = line.split(",")
    r = [r.split("-") for r in ranges]
    return [(int(t[0]), int(t[1])) for t in r]


def parse(lines: list[str]):
    return [line.split("-") for line in lines]


def check_batch(x: str, n: int) -> bool:
    return len(set(batched(x, n))) == 1


def check(x: int) -> int:
    return any(check_batch(str(x), i) for i in range(1, (len(str(x)) // 2) + 1))


def compute(left: int, right: int) -> int:
    return sum(x for x in range(left, right + 1) if check(x))


def main():
    # ranges = read_input("sample.txt")
    ranges = read_input("input.txt")
    result = sum(compute(*rng) for rng in ranges)
    print(result)


if __name__ == "__main__":
    main()
