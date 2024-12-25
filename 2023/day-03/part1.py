import re

SYMBOL = "x"


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def clean_lines(lines):
    def clean_line(line):
        return re.sub(r"[^\d\.]", SYMBOL, line)

    return list(map(clean_line, lines))


def borders_symbol(i, j, S):
    def check_row(row):
        return SYMBOL in S[row][max(j - 1, 0) : min(j + 2, len(S[0]))]

    return any(map(check_row, range(max(i - 1, 0), min(i + 2, len(S)))))


def main():
    lines = read_input("input.txt")
    S = clean_lines(lines)

    sum = 0
    is_adjacent_to_symbol = False

    numbers_to_gears = dict()

    current_num = ""
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j].isdigit():
                current_num += S[i][j]
                if borders_symbol(i, j, S):
                    is_adjacent_to_symbol = True
            else:
                if current_num and is_adjacent_to_symbol:
                    sum += int(current_num)
                    is_adjacent_to_symbol = False
                current_num = ""

    print(sum)


if __name__ == "__main__":
    main()
