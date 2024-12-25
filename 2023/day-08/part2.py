import math
import re
from collections.abc import Iterable
from itertools import cycle
from typing import Dict, List, Set, Tuple

Choice = Tuple[str, str]


def pick(instruction: str) -> int:
    return 0 if instruction == "L" else 1


def read_input(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_line(line: str) -> Tuple[str, Choice]:
    src, left, right = re.findall(r"\w+", line)
    return src, (left, right)


def get_nodes(suffix: str, mapping: Dict[str, Choice]) -> Iterable[str]:
    return filter(lambda key: key[2] == suffix, mapping.keys())


def get_mapping(mapping_lines: List[str]) -> Dict[str, Choice]:
    return dict(map(parse_line, mapping_lines))


def move(src: str, instruction: str, mapping: Dict[str, Choice]) -> str:
    return mapping[src][pick(instruction)]


def compute_cycle(
    src: str,
    instructions: str,
    mapping: Dict[str, Choice],
    dst_nodes: Set[str],
) -> int:
    for step, instruction in enumerate(cycle(instructions), 1):
        src = move(src, instruction, mapping)
        if src in dst_nodes:
            return step
    return 0


def solve(lines: List[str]) -> int:
    instructions = lines[0]
    mapping = get_mapping(lines[2:])

    src_nodes = list(get_nodes("A", mapping))
    dst_nodes = set(get_nodes("Z", mapping))

    cycles = (compute_cycle(src, instructions, mapping, dst_nodes) for src in src_nodes)
    return math.lcm(*cycles)


def main():
    # lines = read_input("sample3.txt")
    lines = read_input("input.txt")
    print(solve(lines))


if __name__ == "__main__":
    main()
