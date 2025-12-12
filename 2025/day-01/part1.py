def read_input(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines


def parse(lines: list[str]):
    return [(r[0], int(r[1:])) for r in lines]


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    init, rotations = 50, parse(lines)

    solution = 0
    acc = init
    for dir, amount in rotations:
        if dir == "R":
            acc = (acc + amount) % 100
        else:
            acc = (acc - amount) % 100
        if acc == 0:
            solution += 1
    print(solution)


if __name__ == "__main__":
    main()
