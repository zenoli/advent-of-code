from collections import defaultdict

GEAR = "*"


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_surrounding_gears(i, j, S):
    return set(
        (row, col)
        for row in range(max(i - 1, 0), min(i + 2, len(S)))
        for col in range(max(j - 1, 0), min(j + 2, len(S[0])))
        if S[row][col] == GEAR
    )


def compute_num_to_gear_mapping(S):
    current_num = ""
    current_bordering_gears = set()
    num_to_gear = defaultdict(set)

    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j].isdigit():
                current_num += S[i][j]
                current_bordering_gears.update(get_surrounding_gears(i, j, S))
            else:
                if current_num:
                    num_to_gear[int(current_num)].update(current_bordering_gears)
                current_num = ""
                current_bordering_gears = set()

    return num_to_gear


def compute_gear_to_num_mapping(num_to_gears):
    gear_to_num = defaultdict(set)

    for num, gears in num_to_gears.items():
        for gear in gears:
            gear_to_num[gear].add(num)

    return gear_to_num


def main():
    S = read_input("input.txt")
    num_to_gear = compute_num_to_gear_mapping(S)
    gear_to_num = compute_gear_to_num_mapping(num_to_gear)

    print(
        sum(
            list(nums)[0] * list(nums)[1]
            for nums in gear_to_num.values()
            if len(nums) == 2
        )
    )


if __name__ == "__main__":
    main()
