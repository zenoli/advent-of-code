from itertools import product, chain
from collections import defaultdict
import math


def read_input(filename):
    flipflops = dict()
    conjunctions = dict()

    def parse(line):
        input, outputs = line.split(" -> ")
        outputs = set(outputs.split(", "))
        if input[0] == "%":
            input = input[1:]
            flipflops[input] = False
        elif input[0] == "&":
            input = input[1:]
            conjunctions[input] = dict()
        return product([input], outputs)

    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    input_mapping, output_mapping = defaultdict(set), defaultdict(set)
    for input, output in chain(*map(parse, lines)):
        input_mapping[output].add(input)
        output_mapping[input].add(output)

    return input_mapping, output_mapping, flipflops, conjunctions


def initialize_conjunctions(input_mapping, conjunctions):
    for name, inputs in input_mapping.items():
        if name in conjunctions:
            conjunctions[name] = {input: False for input in inputs}

    return conjunctions


def solve(input):
    def push_button(flipflops, conjunctions):
        def process(pulse: bool, src: str, dst: str) -> list[tuple[bool, str, str]]:
            if dst in conjunctions:
                conjunctions[dst][src] = pulse
                out_pulse = not all(conjunctions[dst].values())
                return [(out_pulse, dst, new_dest) for new_dest in output_mapping[dst]]
            if dst in flipflops:
                if not pulse:
                    flipflops[dst] = not flipflops[dst]
                    return [
                        (flipflops[dst], dst, new_dest)
                        for new_dest in output_mapping[dst]
                    ]
                return []
            if dst == "broadcaster":
                return [(pulse, dst, new_dest) for new_dest in output_mapping[dst]]
            return []

        tasks: list[tuple[bool, str, str]] = [(False, "button", "broadcaster")]

        count = 0
        while tasks:
            pulse, src, dst = tasks.pop(0)
            count += 1
            tasks.extend(process(pulse, src, dst))
        return flipflops, conjunctions

    input_mapping, output_mapping, flipflops, conjunctions = read_input(input)

    # Maps counter NAND to reset node
    cycle_nodes = {"hd": "hp", "fl": "xv", "kc": "zb", "tb": "qn"}
    counts = dict()

    conjunctions = initialize_conjunctions(input_mapping, conjunctions)
    count = 1
    while not all(nand in counts for nand in cycle_nodes):
        flipflops, conjunctions = push_button(flipflops, conjunctions)
        count += 1
        for nand, reset in cycle_nodes.items():
            if all(v for name, v in conjunctions[nand].items() if name != reset):
                counts[nand] = count

    return math.lcm(*counts.values())


def main():
    res = solve("input.txt")
    print(res)


if __name__ == "__main__":
    main()
