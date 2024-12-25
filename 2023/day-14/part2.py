from functools import reduce, cache
import math
import hashlib
import re

B = 1_000_000_000


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
    print("=======================")


def open_sections(line):
    return ((match.start(), match.end()) for match in re.finditer(r"[\.O]+", line))


def hash(platform):
    return hashlib.sha1("".join(platform).encode("utf-8")).digest()


@cache
def apply_gravity_left(line):
    def gravity(open_section):
        return "".join(reversed(sorted(open_section)))

    out = list(line)
    for start, end in open_sections(line):
        out[start:end] = list(gravity(line[start:end]))
    return "".join(out)


def apply_gravity_right(line):
    def gravity(open_section):
        return "".join(sorted(open_section))

    out = list(line)
    for start, end in open_sections(line):
        out[start:end] = list(gravity(line[start:end]))
    return "".join(out)


def compare_state(old, new):
    return all(row1 == row2 for row1, row2 in zip(old, new))


def total_load(platform):
    return sum((len(platform) - i) * row.count("O") for i, row in enumerate(platform))


def tilt_north(platform):
    return transpose(list(map(apply_gravity_left, transpose(platform))))


def tilt_south(platform):
    return transpose(list(map(apply_gravity_right, transpose(platform))))


def tilt_west(platform):
    return list(map(apply_gravity_left, platform))


def tilt_east(platform):
    return list(map(apply_gravity_right, platform))


def cycle(platform):
    return reduce(
        lambda p, f: f(p), [tilt_north, tilt_west, tilt_south, tilt_east], platform
    )


def main():
    # old = read_input("sample.txt")
    old = read_input("input.txt")
    step = 0
    seen = set()
    cycle_start = -1
    cycle_start_hash = None
    cycle_length = None
    magic_counter = None
    while True:
        step += 1

        new = cycle(old)
        new_hash = hash(new)
        load = total_load(new)

        if cycle_start_hash and cycle_start_hash == new_hash:
            # Patern repeates every `cycle_start + n*cycle_length`
            cycle_length = step - cycle_start
            # Extrapolate at which counter the calculated load
            # will match the billionth iteration
            magic_counter = (
                B - math.floor((B - cycle_start) / cycle_length) * cycle_length
            ) + cycle_length

        if not cycle_start_hash and new_hash in seen:
            # Cycle detected!
            cycle_start = step
            cycle_start_hash = new_hash

        if step == magic_counter:
            print(load)
            break
        seen.add(new_hash)
        old = new


if __name__ == "__main__":
    main()
