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


def get_block(condition):
    d = defaultdict(lambda: (1, 4001))
    if condition is None:
        return d

    category, op, thresh = condition.values()
    if op == "<":
        d[category] = (1, thresh)
    else:
        d[category] = (thresh + 1, 4001)
    return d


def invert_condition(condition):
    category, op, thresh = condition.values()
    if op == "<":
        return {"category": category, "op": ">", "thresh": thresh - 1}
    else:
        return {"category": category, "op": "<", "thresh": thresh + 1}


def generate_constraint_blocks(rules):
    next_constraint_block = get_block(None)
    blocks = []
    for condition, state in rules[:-1]:
        block = intersect(get_block(condition), next_constraint_block)
        next_constraint_block = intersect(
            get_block(invert_condition(condition)), next_constraint_block
        )
        blocks.append((block, state))

    blocks.append((next_constraint_block, rules[-1][1]))
    return blocks


def intersect(block1, block2):
    def intersect_interval(a, b):
        a0, a1 = a
        b0, b1 = b
        return (max(a0, b0), min(a1, b1))

    return {
        category: intersect_interval(block1[category], block2[category])
        for category in "xmas"
    }


def is_valid_block(block):
    return all(start < end for (start, end) in block.values())


def volume(*ranges):
    def diff(r):
        start, end = r[0], r[1]
        return end - start

    return prod(map(diff, ranges))


def update_constraint(condition, constraint):
    category, op, thresh = condition.values()
    low, hi = constraint[category]
    if op == "<":
        hi = min(hi, thresh)
    else:
        low = max(low, thresh + 1)

    if low < hi:
        constraint[category] = (low, hi)
        return constraint
    else:
        return None


def update_constraints(condition, constraints):
    return list(map(lambda c: update_constraint(condition, c), constraints))


def get_constraints(state, workflows):
    if state == "A":
        return [{x: (1, 4001), m: (1, 4001), a: (1, 4001), s: (1, 4001)}]

    constraints = []
    for constraint_block, out_state in workflows[state]:
        if out_state == "R":
            continue
        neighbor_constraints = get_constraints(out_state, workflows)
        constraints.extend(
            [intersect(constraint_block, c) for c in neighbor_constraints]
        )

    return constraints


def solve(input):
    workflows, _ = read_input(input)
    constraint_blocks_dict = {
        state: generate_constraint_blocks(rules) for state, rules in workflows.items()
    }

    constraints = get_constraints("in", constraint_blocks_dict)
    res = 0
    for c in constraints:
        res += volume(*c.values())
    return res


def main():
    print(solve("input.txt"))


if __name__ == "__main__":
    main()
