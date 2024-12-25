import re


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def solve_line(line):
    line_inv = line[::-1]

    first_digit, last_digit = "", ""

    if first_digit_search := re.search(r"\d", line):
        first_digit = line[first_digit_search.start()]
    else:
        return 0

    if last_digit_search := re.search(r"\d", line_inv):
        last_digit = line_inv[last_digit_search.start()]

    return int(first_digit + last_digit)


def solve(lines):
    print(sum(map(solve_line, lines)))


def main():
    # lines = read_input("input.txt")
    lines = read_input("sample-part1.txt")
    solve(lines)


if __name__ == "__main__":
    main()
