def read_input(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    line = lines[0]
    ranges = line.split(",")
    r = [r.split("-") for r in ranges]
    return [(int(t[0]), int(t[1])) for t in r]


def parse(lines: list[str]):
    return [line.split("-") for line in lines]


def check(x: str):
    if len(x) % 2 != 0:
        return False
    mid = len(x) // 2
    return x[:mid] == x[mid:]


def compute(left: int, right: int) -> int:
    return sum(x for x in range(left, right + 1) if check(str(x)))


def main():
    ranges = read_input("input.txt")
    result = sum(compute(*rng) for rng in ranges)
    print(result)


if __name__ == "__main__":
    main()
