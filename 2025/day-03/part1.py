def read_input(filename: str):
    with open(filename) as file:
        lines = [list(map(int, line.strip())) for line in file]
    return lines


def argmax(xs: list[int]):
    idx = 0
    mx = 0
    for i, x in enumerate(xs):
        if x > mx:
            idx = i
            mx = x
    return mx, idx


def joltage(bank: list[int]) -> int:
    first, idx = argmax(bank[:-1])
    second = max(bank[idx + 1 :])
    return int(f"{first}{second}")


def main():
    # banks = read_input("sample.txt")
    banks = read_input("input.txt")
    print(sum(joltage(bank) for bank in banks))


if __name__ == "__main__":
    main()
