def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_numbers(line):
    def get_set(number_list):
        return set(map(int, number_list.split()))

    left, right = line.split("|")
    return get_set(left.split(":")[1]), get_set(right)


def compute_score(winning, ours):
    x = len(winning.intersection(ours))
    return 2 ** (x - 1) if x else 0


def solve(lines):
    return sum(
        compute_score(winning, ours) for winning, ours in map(get_numbers, lines)
    )


def main():
    lines = read_input("sample.txt")
    # lines = read_input("input.txt")
    print(solve(lines))
    pass


if __name__ == "__main__":
    main()
