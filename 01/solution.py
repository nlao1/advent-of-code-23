from parse import parse_input, parse_input_pt2
from typing import Generator

example = parse_input("example.txt")
input = parse_input("input.txt")

example2 = parse_input_pt2("example2.txt")
input2 = parse_input_pt2("input.txt")

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits = list(map(lambda x: str(x), digits))


def first_number_in_line(s) -> int:
    for c in s:
        if c in digits:
            return int(c)
    return 0


def solution_pt1(input: Generator[str, None, None]):
    sum = 0
    for line in input:
        line_number = 10 * first_number_in_line(line) + first_number_in_line(line[::-1])
        sum += line_number
    return sum


if __name__ == "__main__":
    print(solution_pt1(input))
    print(solution_pt1(example2))
    print(solution_pt1(input2))
