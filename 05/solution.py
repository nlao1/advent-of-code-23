import parse
from typing import List, Tuple


def part1_solution(filename):
    plant_converter = parse.parse_input(filename)
    min_seed = min(
        plant_converter.seeds,
        key=lambda x: plant_converter.follow_lifecycle_to_location(x),
    )
    return plant_converter.follow_lifecycle_to_location(min_seed)


def part2_solution(filename):
    # seed ranges are now encoded as tuples, both endpoints inclusive
    plant_converter = parse.parse_input(filename)
    original_seeds = plant_converter.seeds
    new_seeds = [
        (original_seeds[i], original_seeds[i + 1] - 1)
        for i in range(0, len(original_seeds), 2)
    ]
    # convert to ranges
    new_seeds = list(map(lambda x: (x[0], x[0] + x[1]), new_seeds))
    rangeset: parse.RangeSet = parse.RangeSet(set(new_seeds))
    output_rangeset = plant_converter.follow_lifecycle_to_location_range(rangeset)
    min_location = min(output_rangeset.get_ranges())
    return min_location


if __name__ == "__main__":
    print(part1_solution("example.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example.txt"))
    print(part2_solution("input.txt"))
