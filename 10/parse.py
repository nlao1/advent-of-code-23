from typing import List, Tuple, Dict
from collections import defaultdict

DOWN = (1, 0)
UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

character_to_directions = {
    ".": [],
    "F": [DOWN, RIGHT],
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "J": [LEFT, UP],
    "7": [LEFT, DOWN],
    "L": [UP, RIGHT],
    # I think you can just assume that S connects to everything because in the
    # graph we will assume that edges only exist if they are bidirectional
    "S": [UP, DOWN, LEFT, RIGHT],
}


def in_bounds(width, height, row, col):
    return row >= 0 and row < height and col >= 0 and col < width


def parse_input(
    filename,
) -> Tuple[Tuple[int, int], Dict[Tuple[int, int], List[Tuple[int, int]]]]:
    graph = {}
    matrix = []
    with open(filename) as f:
        for line in f:
            matrix.append([*line.strip()])
    height = len(matrix)
    width = len(matrix[0])
    animal_position = None
    for row_idx, row in enumerate(matrix):
        for col_idx, tile in enumerate(row):
            graph[(row_idx, col_idx)] = []
            if tile == "S":
                animal_position = (row_idx, col_idx)
            for row_offset, col_offset in character_to_directions[tile]:
                neighbor = (row_idx + row_offset, col_idx + col_offset)
                if in_bounds(width, height, *neighbor):
                    graph[(row_idx, col_idx)].append(neighbor)
    return animal_position, graph


# print(*parse_input("simple_example.txt").items(), sep="\n")
# print(*parse_input("simple_example_extra.txt").items(), sep="\n")
