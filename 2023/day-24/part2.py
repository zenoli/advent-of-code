import numpy as np
import z3


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]

    return list(map(parse, lines))


def parse(line):
    def to_tuple(s):
        return tuple(np.array(list(map(int, s.split(","))))[:3])

    return tuple(map(to_tuple, line.split("@")))


def solve(input):
    lines = read_input(input)

    s = z3.Solver()

    pv_1 = z3.Int("p1")
    pv_2 = z3.Int("p2")
    pv_3 = z3.Int("p3")

    dv_1 = z3.Int("d1")
    dv_2 = z3.Int("d2")
    dv_3 = z3.Int("d3")

    xs = []

    for i, ((p1, p2, p3), (d1, d2, d3)) in enumerate(lines):
        x = z3.Int(f"x{i}")
        xs.append(x)
        s.add(p1 + x * d1 == pv_1 + x * dv_1)
        s.add(p2 + x * d2 == pv_2 + x * dv_2)
        s.add(p3 + x * d3 == pv_3 + x * dv_3)

    print(s.check())

    m = s.model()

    return m[pv_1].as_long() + m[pv_2].as_long() + m[pv_3].as_long()  # pyright: ignore


def main():
    res = solve("input.txt")
    # res = solve("sample.txt")
    print(res)


if __name__ == "__main__":
    main()
