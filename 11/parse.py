from typing import Dict, Tuple, Set

DOWN = (1, 0)
UP = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [DOWN, UP, LEFT, RIGHT]


def in_bounds(width, height, row, col):
    return row >= 0 and row < height and col >= 0 and col < width


def edge_weight_of_neighbors(
    row, col, empty_row_idxs, empty_col_idxs, expansion_factor
):
    weights = {}
    for row_offset, col_offset in DIRECTIONS:
        weight_is_two = (col_offset == 0 and row in empty_row_idxs) or (
            row_offset == 0 and col in empty_col_idxs
        )
        weights[(row + row_offset, col + col_offset)] = (
            expansion_factor if weight_is_two else 1
        )
    return weights


def parse_input(
    filename: str, expansion_factor: int
) -> Tuple[Dict[Tuple[int, int], Dict[Tuple[int, int], float]], Set[Tuple[int, int]]]:
    graph = {}
    matrix = []
    galaxies = set()
    with open(filename) as f:
        for line in f:
            matrix.append([*line.strip()])
    height = len(matrix)
    width = len(matrix[0])
    empty_row_idxs = {
        row_idx for row_idx, row in enumerate(matrix) if all(x == "." for x in row)
    }
    empty_col_idxs = {
        col_idx
        for col_idx in range(width)
        if all(row[col_idx] == "." for row in matrix)
    }
    for row_idx, row in enumerate(matrix):
        for col_idx, tile in enumerate(row):
            graph[(row_idx, col_idx)] = {}
            if tile == "#":
                galaxies.add((row_idx, col_idx))
            for neighbor, weight in edge_weight_of_neighbors(
                row_idx, col_idx, empty_row_idxs, empty_col_idxs, expansion_factor
            ).items():
                if in_bounds(width, height, *neighbor):
                    graph[(row_idx, col_idx)][neighbor] = weight
    return dict(graph), galaxies
