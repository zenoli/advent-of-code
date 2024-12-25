import re
from itertools import cycle


def pick(instruction):
    return 0 if instruction == "L" else 1


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_line(line):
    src, left, right = re.findall(r"\w+", line)
    return src, (left, right)


def get_mapping(mapping_lines):
    return dict(map(parse_line, mapping_lines))


def move(src, instruction, mapping):
    return mapping[src][pick(instruction)]


def solve(lines):
    instructions = lines[0]
    mapping = get_mapping(lines[2:])

    src = "AAA"
    dst = "ZZZ"
    for step, instruction in enumerate(cycle(instructions), 1):
        src = move(src, instruction, mapping)
        if src == dst:
            print(step)
            break


def main():
    # lines = read_input("sample2.txt")
    lines = read_input("input.txt")
    solve(lines)


if __name__ == "__main__":
    main()
