import re


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def transpose(platform):
    def col(j):
        return "".join(platform[i][j] for i in range(len(platform)))

    return [col(j) for j in range(len(platform[0]))]


def debug(lines):
    for line in lines:
        print(line)


def open_sections(line):
    return ((match.start(), match.end()) for match in re.finditer(r"[\.O]+", line))


def apply_gravity(line):
    def gravity(open_section):
        return "".join(reversed(sorted(open_section)))

    out = list(line)
    for start, end in open_sections(line):
        out[start:end] = list(gravity(line[start:end]))
    return "".join(out)


def main():
    # platform = read_input("sample.txt")
    platform = read_input("input.txt")

    debug(transpose(list(map(apply_gravity, transpose(platform)))))
    tilted_platform = transpose(list(map(apply_gravity, transpose(platform))))
    result = sum(
        (len(tilted_platform) - i) * row.count("O")
        for i, row in enumerate(tilted_platform)
    )

    print(result)


if __name__ == "__main__":
    main()
