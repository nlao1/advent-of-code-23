from typing import List, Tuple
import parse

example = parse.parse_input("example.txt")
input = parse.parse_input("input.txt")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def find_max_in_game(game: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
    max_red_in_game = max(game, key=lambda x: x[0])[0]
    max_green_in_game = max(game, key=lambda x: x[1])[1]
    max_blue_in_game = max(game, key=lambda x: x[2])[2]
    return (max_red_in_game, max_green_in_game, max_blue_in_game)


def part1_solution(input: List[Tuple[int, List[Tuple[int, int, int]]]]):
    answer = 0
    for game_num, game in input:
        game_max_red, game_max_green, game_max_blue = find_max_in_game(game)
        if (
            game_max_blue <= MAX_BLUE
            and game_max_green <= MAX_GREEN
            and game_max_red <= MAX_RED
        ):
            answer += game_num
    return answer


def part2_solution(input: List[Tuple[int, List[Tuple[int, int, int]]]]):
    sum_of_powers = 0
    for _game_num, game in input:
        game_max_red, game_max_green, game_max_blue = find_max_in_game(game)
        power = game_max_red * game_max_green * game_max_blue
        sum_of_powers += power
    return sum_of_powers


if __name__ == "__main__":
    # print(part1_solution(example))
    print(part1_solution(input))
    # print(part2_solution(example))
    print(part2_solution(input))
