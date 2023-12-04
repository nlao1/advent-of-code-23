from typing import List, Tuple


def parse_input(filename) -> List[Tuple[int, List[int], List[int]]]:
    with open(filename) as f:
        output = []
        for line in f:
            card_info, card_numbers_str = line.strip().split("|")
            card_id_str, card_winning_numbers_str = card_info.split(":")
            card_winning_numbers = filter(
                lambda x: len(x) > 0, card_winning_numbers_str.strip().split(" ")
            )
            card_id = card_id_str.strip().split(" ")[-1]
            card_numbers_str = filter(
                lambda x: len(x) > 0, card_numbers_str.strip().split(" ")
            )
            output.append(
                (
                    int(card_id),
                    [int(x) for x in card_winning_numbers],
                    [int(x) for x in card_numbers_str],
                )
            )
        return output
