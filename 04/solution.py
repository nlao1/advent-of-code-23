import parse
from typing import List, Tuple


def part1_solution(filename):
    input = parse.parse_input(filename)
    total_value = 0
    for _card_id, card_winning_numbers, card_numbers in input:
        # set for faster access
        card_winning_numbers = set(card_winning_numbers)
        card_numbers_in_winning_numbers = filter(
            lambda x: x in card_winning_numbers, card_numbers
        )
        winning_numbers_count = len(list(card_numbers_in_winning_numbers))
        total_value += (
            2 ** (winning_numbers_count - 1) if winning_numbers_count > 0 else 0
        )
    return total_value


def part2_solution(filename):
    input = parse.parse_input(filename)
    total_scratchcards = 0
    count_of_scratchcard = {info[0]: 1 for info in input}
    for card_id, card_winning_numbers, card_numbers in input:
        curr_scratchcard_count = count_of_scratchcard[card_id]
        total_scratchcards += curr_scratchcard_count
        card_winning_numbers = set(card_winning_numbers)
        card_numbers_in_winning_numbers = filter(
            lambda x: x in card_winning_numbers, card_numbers
        )
        winning_numbers_count = len(list(card_numbers_in_winning_numbers))
        for i in range(1, winning_numbers_count + 1):
            count_of_scratchcard[card_id + i] += curr_scratchcard_count
    return total_scratchcards


if __name__ == "__main__":
    print(part1_solution("example.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example.txt"))
    print(part2_solution("input.txt"))
