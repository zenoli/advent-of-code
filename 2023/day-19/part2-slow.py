from itertools import product, chain, pairwise
from collections import defaultdict
from typing import OrderedDict
from math import prod

x, m, a, s = "xmas"


def read_input(filename):
    def parse_part(part):
        return eval(part.replace("=", ":"))

    def parse_workflow(workflow_str):
        def parse_rule(rule_str):
            def parse_condition(cond_str):
                return {
                    "category": cond_str[0],
                    "op": cond_str[1],
                    "thresh": int(cond_str[2:]),
                }

            rule = rule_str.split(":")
            if len(rule) == 1:
                return None, rule[0]
            else:
                cond_str, state = rule
                return parse_condition(cond_str), state

        name, rules = workflow_str.split("{")
        rules_str = rules[:-1]
        rules = rules_str.split(",")
        return name, list(map(parse_rule, rules))

    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    sep = lines.index("")
    workflows, parts = lines[:sep], lines[sep + 1 :]
    return dict(map(parse_workflow, workflows)), list(map(parse_part, parts))


def process(part, workflows):
    # print(part)

    def step(part, state, workflows):
        for condition, dest in workflows[state]:
            if not condition:
                return dest
            if eval(
                f"{part[condition['category']]} {condition['op']} {condition["thresh"]}"
            ):
                return dest

    state = "in"
    while state not in ["R", "A"]:
        state = step(part, state, workflows)
    return state


def extract_partitions(workflows):
    def extract(rules):
        conditions = (condition.values() for condition, _ in rules if condition)
        return {
            category: thresh + (0 if op == "<" else 1)
            for (category, op, thresh) in conditions
        }

    partitions = defaultdict(lambda: set([1, 4001]))

    for category, value in chain(
        *map(lambda x: x.items(), map(extract, workflows.values()))
    ):
        partitions[category].add(value)

    partitions_sorted = OrderedDict()
    for category in "xmas":
        partitions_sorted[category] = sorted(partitions[category])
    return partitions_sorted


def volume(*ranges):
    def diff(r):
        start, end = r[0], r[1]
        return end - start

    return prod(map(diff, ranges))


def main():
    # workflows, parts = read_input("sample.txt")
    workflows, _ = read_input("input.txt")
    partitions = extract_partitions(workflows)

    print(partitions)
    res = 0
    N = prod(map(len, partitions.values()))
    print("N: ", N)
    for i, (x, m, a, s) in enumerate(product(*map(pairwise, partitions.values()))):
        if i % 100000 == 0:
            print(f"[{i}/{N}]")
        # print(x, m, a, s)
        state = process({"x": x[0], "m": m[0], "a": a[0], "s": s[0]}, workflows)
        if state == "A":
            res += volume(x, m, a, s)

    print(res)


if __name__ == "__main__":
    main()
