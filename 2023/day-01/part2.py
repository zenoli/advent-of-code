import re

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_pattern_forward():
    return re.compile("|".join([r"\d"] + list(digits.keys())))


def get_pattern_inv():
    keys_inv = list(map(lambda digit: digit[::-1], digits.keys()))
    return re.compile("|".join([r"\d"] + keys_inv))


def solve_line(line):
    line_inv = line[::-1]

    first_digit, last_digit = "", ""

    if first_digit_search := get_pattern_forward().search(line):
        first_digit = line[first_digit_search.start() : first_digit_search.end()]
        if first_digit in digits:
            first_digit = digits[first_digit]
    else:
        return 0

    if last_digit_search := get_pattern_inv().search(line_inv):
        last_digit = line_inv[last_digit_search.start() : last_digit_search.end()]
        last_digit = last_digit[::-1]
        if last_digit in digits:
            last_digit = digits[last_digit]

    return int(first_digit + last_digit)


def solve(lines):
    print(sum(map(solve_line, lines)))


def main():
    lines = read_input("input.txt")
    # lines = read_input("sample-part2.txt")
    solve(lines)


if __name__ == "__main__":
    digits.keys()
    main()
