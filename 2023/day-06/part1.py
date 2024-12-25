import re
import math

EPS = 0.0001

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_numbers(line):
    return list(map(int, re.findall(r"\d+", line)))


def solve(lines):
    return math.prod(
        compute_solutions(time, distance)
        for time, distance in zip(*map(parse_numbers, lines))
    )


def compute_solutions(time, distance):
    determinant = math.sqrt(time * time - 4 * distance)
    solutions = ((time + determinant) * 0.5, (time - determinant) * 0.5)

    return  math.floor(max(solutions) - EPS) - math.ceil(min(solutions) + EPS) + 1


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    print(solve(lines))


if __name__ == "__main__":
    main()
