import parse
from itertools import pairwise


def get_difference_list(history):
    return [y - x for x, y in pairwise(history)]


def compute_next_value(history) -> int:
    """
    A history is a sequence of some kind defined in the problem.
    """
    # you can shortcut this by 1 call if you make the base case just when the
    # differences are all equal
    if all(x == 0 for x in history):
        return 0
    differences = get_difference_list(history)
    return history[-1] + compute_next_value(differences)


def sum_of_extrapolated_values(histories):
    return sum(compute_next_value(history) for history in histories)


def part1_solution(filename):
    return sum_of_extrapolated_values(parse.parse_input(filename))


def part2_solution(filename):
    histories = parse.parse_input(filename)
    # reversed_histories = list(map(lambda l: list(reversed(l)), histories))
    reversed_histories = [l[::-1] for l in histories]
    return sum_of_extrapolated_values(reversed_histories)


if __name__ == "__main__":
    print(part1_solution("example.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example.txt"))
    print(part2_solution("input.txt"))
