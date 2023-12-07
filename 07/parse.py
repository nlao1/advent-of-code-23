from typing import List, Tuple


def parse_input(filename) -> List[Tuple[List[str], int]]:
    hands = []
    with open(filename) as f:
        for line in f:
            cards_str, wager_str = line.strip().split(" ")
            wager = int(wager_str.strip())
            cards = list(cards_str)
            hands.append((cards, wager))
    return hands
