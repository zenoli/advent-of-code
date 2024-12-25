from itertools import product, chain
from collections import defaultdict


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
    def process(pulse, src, dst):
        if dst in conjunctions:
            conjunctions[dst][src] = pulse
            out_pulse = not all(conjunctions[dst].values())
            return [(out_pulse, dst, new_dest) for new_dest in output_mapping[dst]]
        if dst in flipflops:
            if not pulse:
                flipflops[dst] = not flipflops[dst]
                return [
                    (flipflops[dst], dst, new_dest) for new_dest in output_mapping[dst]
                ]
            return []
        if dst == "broadcaster":
            return [(pulse, dst, new_dest) for new_dest in output_mapping[dst]]
        return []

    def push_button():
        tasks = [(False, "button", "broadcaster")]

        while tasks:
            pulse, src, dst = tasks.pop(0)
            if pulse:
                pulses["high"] += 1
            else:
                pulses["low"] += 1

            # print(f"{src} -{'high' if pulse else 'low'}-> {dst}")
            tasks.extend(process(pulse, src, dst))

    input_mapping, output_mapping, flipflops, conjunctions = read_input(input)
    conjunctions = initialize_conjunctions(input_mapping, conjunctions)

    pulses = {"low": 0, "high": 0}
    for _ in range(1000):
        push_button()

    return pulses["low"] * pulses["high"]


def main():
    state = {}
    res = solve("input.txt")
    print(res)


if __name__ == "__main__":
    main()
