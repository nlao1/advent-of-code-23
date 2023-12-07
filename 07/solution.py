import parse
from typing import List, Tuple, Dict
from functools import cmp_to_key, partial

card_to_value_part1 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

card_to_value_part2 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 0,
    "Q": 12,
    "K": 13,
    "A": 14,
}


hand_type_to_ranking = {
    "5 of a kind": 6,
    "4 of a kind": 5,
    "full house": 4,
    "3 of a kind": 3,
    "two pair": 2,
    "one pair": 1,
    "high card": 0,
}


def find_doubles(hand_counts: Dict[str, int], is_joker_wildcard):
    """
    finds number of pairs in the hand and returns them in order of occurrence
    """
    number_of_doubles = 0
    doubles = []
    for k, v in hand_counts.items():
        if is_joker_wildcard:
            if v == 2:
                number_of_doubles += 1
                doubles.append(k)
            elif (
                v <= 2
                and "J" in hand_counts
                and hand_counts["J"] + v == 2
                and hand_counts["J"] > 0
            ):
                hand_counts["J"] -= 2 - v
                number_of_doubles += 1
                doubles.append(k)
        else:
            if v == 2:
                number_of_doubles += 1
                doubles.append(k)

    return number_of_doubles, doubles


def classify_hand_part1(hand: List[str]) -> Tuple[str, str]:
    counts = {}
    triple = None
    for card in hand:
        count_of_card = hand.count(card)
        counts[card] = count_of_card
        # 4 and 5 of a kind can be dealt with easily
        if count_of_card == 5:
            return "5 of a kind", card
        elif count_of_card == 4:
            return "4 of a kind", card
        elif count_of_card == 3:
            triple = card
    number_of_doubles, doubles = find_doubles(counts, False)
    if triple is not None:
        if number_of_doubles > 0:
            # for full house return a concatenated string of triple double
            return "full house", f"{triple},{doubles[0]}"
        else:
            return "3 of a kind", triple
    if number_of_doubles == 2:
        # returns pairs in order of occurrence
        return "two pair", f"{doubles[0]},{doubles[1]}"
    if number_of_doubles == 1:
        return "one pair", doubles[0]
    return "high card", max(hand, key=lambda x: card_to_value_part1[x])


def classify_hand_part2(hand: List[str]) -> Tuple[str, str]:
    counts: Dict[str, int] = {card: hand.count(card) for card in hand}
    # most frequent cards will appear first
    counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    triple = None
    if len(counts) == 2 and "J" in counts:
        return "5 of a kind", "J"
    for card, count in counts.items():
        if ("J" in counts and count + counts["J"] == 5 and card != "J") or count == 5:
            return "5 of a kind", card
        elif "J" in counts and count + counts["J"] == 4 and card != "J" or count == 4:
            return "4 of a kind", card
        elif "J" in counts and count + counts["J"] == 3 and card != "J" or count == 3:
            triple = card
            if count < 3:
                counts["J"] -= 3 - count
                counts[card] = 3
    number_of_doubles, doubles = find_doubles(counts, True)
    assert "J" not in counts or counts["J"] >= 0
    if triple is not None:
        if number_of_doubles > 0:
            # for full house return a concatenated string of triple double
            return "full house", f"{triple},{doubles[0]}"
        else:
            return "3 of a kind", triple
    if number_of_doubles == 2:
        # returns pairs in order of occurrence
        return "two pair", f"{doubles[0]},{doubles[1]}"
    if number_of_doubles == 1:
        return "one pair", doubles[0]
    return "high card", max(hand, key=lambda x: card_to_value_part2[x])


def compare_hands(part, hand1, hand2):
    hand1, _, (class1, _) = hand1
    hand2, _, (class2, _) = hand2
    rank1 = class1
    rank2 = class2
    numerical_rank1 = hand_type_to_ranking[rank1]
    numerical_rank2 = hand_type_to_ranking[rank2]
    if numerical_rank1 > numerical_rank2:
        return 1
    elif numerical_rank1 < numerical_rank2:
        return -1
    # if same, compare card-by-card
    card_to_value = card_to_value_part1 if part == 1 else card_to_value_part2
    for hand1_card, hand2_card in zip(hand1, hand2):
        hand1_card_value = card_to_value[hand1_card]
        hand2_card_value = card_to_value[hand2_card]
        if hand1_card_value > hand2_card_value:
            return 1
        elif hand1_card_value < hand2_card_value:
            return -1
    # if the hands are equal, arbitrarily return 1
    return 1


def part1_solution(filename):
    input = parse.parse_input(filename)
    input = [(hand, wager, classify_hand_part1(hand)) for (hand, wager) in input]
    input.sort(key=cmp_to_key(partial(compare_hands, 1)))
    winnings = 0
    for i, (_, wager, _) in enumerate(input):
        winnings += (i + 1) * wager
    return winnings


def part2_solution(filename):
    input = parse.parse_input(filename)
    input = [(hand, wager, classify_hand_part2(hand)) for (hand, wager) in input]
    input.sort(key=cmp_to_key(partial(compare_hands, 2)))
    # print(*input, sep="\n")
    winnings = 0
    for i, (_, wager, _) in enumerate(input):
        winnings += (i + 1) * wager
    return winnings


if __name__ == "__main__":
    print(part1_solution("example.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example.txt"))
    print(part2_solution("input.txt"))
