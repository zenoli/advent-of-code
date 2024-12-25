def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


X, c = "", []
memo = {}


def f(i, j):
    if j == len(c):
        return 0 if "#" in X[i:] else 1
    if i >= len(X):
        return 0

    res = 0
    if X[i] in "?#" and can_place(i, c[j]):
        key = (i + c[j] + 1, j + 1)
        if key not in memo:
            tmp = f(*key)
            memo[key] = tmp
        res += memo[key]

    if X[i] in "?.":
        key = (i + 1, j)
        if key not in memo:
            tmp = f(*key)
            memo[key] = tmp
        res += memo[key]
    return res


def can_place(i, group):
    if len(X[i:]) < group:
        return False
    if len(X[i:]) > group and X[i + group] == "#":
        return False
    return set(X[i : i + group]) <= {"#", "?"}


def parse_line2(line):
    record, groups = line.split()
    groups = list(map(int, ((groups + ",") * 5)[:-1].split(",")))
    return "?".join([record] * 5), groups


def parse_line(line):
    record, groups = line.split()
    groups = list(map(int, groups.split(",")))
    return record, groups


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    global X
    global c
    global memo

    total = 0
    for record, group in map(parse_line2, lines):
        X = record
        c = group
        memo = {}
        result = f(0, 0)
        total += result

    print(total)


if __name__ == "__main__":
    main()
