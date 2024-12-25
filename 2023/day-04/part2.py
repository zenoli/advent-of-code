def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_matches(line):
    def get_set(number_list):
        return set(map(int, number_list.split()))

    left, right = line.split("|")
    return get_matching_numbers(get_set(left.split(":")[1]), get_set(right))


def get_matching_numbers(winning, ours):
    return len(winning.intersection(ours))


def initialize_card_counts(lines):
    card_counts = [1] * (len(lines) + 1)
    card_counts[0] = 0
    return card_counts


def main():
    lines = read_input("input.txt")
    # lines = read_input("sample.txt")
    card_counts = initialize_card_counts(lines)
    match_counts = [0] + list(map(get_matches, lines))

    for i in range(1, len(lines) + 1):
        for j in range(i + 1, min(i + match_counts[i] + 1, len(match_counts))):
            card_counts[j] += card_counts[i]

    print(sum(card_counts))


if __name__ == "__main__":
    main()
