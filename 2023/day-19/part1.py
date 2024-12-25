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
    if state == "A":
        return sum(part.values())
    else:
        return 0


def main():
    # workflows, parts = read_input("sample.txt")
    workflows, parts = read_input("input.txt")
    result = sum(map(lambda part: process(part, workflows), parts))
    print(result)


if __name__ == "__main__":
    main()
