from functools import cache, reduce
from collections import defaultdict, OrderedDict


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines[0].split(",")


@cache
def parse(step):
    split = step.split("=")
    return (split[0], "=", int(split[1])) if len(split) == 2 else (step[:-1], "-", None)


def hash(label):
    def f(a, b):
        return (a + b) * 17 % 256

    return reduce(f, map(ord, label), 0)


def remove(label, boxes):
    if label in boxes[hash(label)]:
        del boxes[hash(label)][label]


def upsert(label, focal_length, boxes):
    boxes[hash(label)][label] = focal_length


def initialize(sequence):
    boxes = defaultdict(OrderedDict)
    for label, op, fl in map(parse, sequence):
        if op == "=":
            upsert(label, fl, boxes)
        else:
            remove(label, boxes)
    return boxes


def focusing_power(boxes):
    return sum(
        (box_nr + 1) * (slot_nr) * focal_length
        for box_nr, lenses in boxes.items()
        for slot_nr, (_, focal_length) in enumerate(lenses.items(), start=1)
    )


def main():
    # sequence = read_input("sample.txt")
    sequence = read_input("input.txt")

    boxes = initialize(sequence)
    result = focusing_power(boxes)
    print(result)


if __name__ == "__main__":
    main()
