from typing import List, Tuple, Dict
import parse


def adjacent_coordinates(point):
    row, col = point
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                yield (row + i, col + j)


def part1_solution(filename):
    coord_to_data, symbol_indices = parse.parse_input(filename)
    sum = 0
    for symbol_location, _ in symbol_indices:
        seen_locations = set()
        for row, col in adjacent_coordinates(symbol_location):
            if (row, col) in coord_to_data and (row, col) not in seen_locations:
                number, index_in_number = coord_to_data[(row, col)]
                col_start = col - index_in_number
                seen_locations |= set(
                    [(row, col_start + i) for i in range(len(str(number)))]
                )
                sum += number
    return sum


def part2_solution(filename):
    coord_to_data, symbol_indices = parse.parse_input(filename)
    sum_of_product_gears = 0
    for symbol_location, symbol in filter(lambda x: x[1] == "*", symbol_indices):
        seen_locations = set()
        part_numbers = []
        for row, col in adjacent_coordinates(symbol_location):
            if (row, col) in coord_to_data and (row, col) not in seen_locations:
                number, index_in_number = coord_to_data[(row, col)]
                col_start = col - index_in_number
                seen_locations |= set(
                    [(row, col_start + i) for i in range(len(str(number)))]
                )
                part_numbers.append(coord_to_data[(row, col)][0])
        if len(part_numbers) == 2:
            sum_of_product_gears += part_numbers[0] * part_numbers[1]
    return sum_of_product_gears


if __name__ == "__main__":
    print(part1_solution("example.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example.txt"))
    print(part2_solution("input.txt"))
