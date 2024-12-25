import math
from collections import Counter
from functools import cmp_to_key
from operator import itemgetter

# Sort-indices
FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def card_rank(card):
    card_ranks = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
        "T": 10,
    }

    return card_ranks[card] if card in card_ranks else int(card)


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_line(line):
    hand, bid = line.split()
    bid = int(bid)
    return hand, bid


def card_counts_without_joker(hand):
    card_counts_without_joker = list(filter(lambda x: x[0] != "J", Counter(hand).most_common()))
    return card_counts_without_joker


def get_strength(hand):
    counter = Counter(hand)
    if counter["J"] == 5:
        return FIVE_OF_A_KIND
    counts_no_joker = card_counts_without_joker(hand)
    most_common_card_count = counts_no_joker[0][1] + counter["J"]
    num_unique_cards = len(counts_no_joker)
    if most_common_card_count == 5:
        return FIVE_OF_A_KIND
    if most_common_card_count == 4:
        return FOUR_OF_A_KIND
    if most_common_card_count == 3:
        return FULL_HOUSE if num_unique_cards == 2 else THREE_OF_A_KIND
    if most_common_card_count == 2:
        return TWO_PAIR if num_unique_cards == 3 else ONE_PAIR
    else:
        return HIGH_CARD


def wrap(f):
    def compare_hand_bid_tuples(hand_bid1, hand_bid2):
        return f(hand_bid1[0], hand_bid2[0])

    return compare_hand_bid_tuples


def compare_hands(hand1, hand2):
    def rank_list(hand):
        return list(map(card_rank, list(hand)))

    cmp_strength = get_strength(hand1) - get_strength(hand2)
    if cmp_strength:
        return cmp_strength
    else:
        cmp_cards = rank_list(hand1) < rank_list(hand2)
        return -1 if cmp_cards else 1


def solve(lines):
    return sum(
        map(
            math.prod,
            enumerate(
                map(
                    itemgetter(1),
                    sorted(map(parse_line, lines), key=cmp_to_key(wrap(compare_hands))),
                ),
                1,
            ),
        )
    )


def main():
    # lines = read_input("sample.txt")
    lines = read_input("input.txt")
    print(solve(lines))


if __name__ == "__main__":
    main()
