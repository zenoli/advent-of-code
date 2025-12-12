from operator import add, sub


def read_input(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines


def parse(lines: list[str]):
    return [(sub if r[0] == "L" else add, int(r[1:])) for r in lines]


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    init, rotations = 50, parse(lines)

    solution = 0
    acc = init
    size = 100
    for op, amount in rotations:
        full_rots, remainder = amount // size, amount % size
        acc_raw = op(acc, remainder)

        if acc != 0 and (acc_raw < 0 or acc_raw > size):
            solution += 1
        acc = acc_raw % size
        if acc == 0:
            solution += 1
        solution += full_rots
        print(f"{acc_raw=}, {acc=}, {amount=} {full_rots=}, {remainder=}")
    print(solution)


if __name__ == "__main__":
    main()
