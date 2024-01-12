from parse import parse_input
from typing import Dict, Tuple, List, Set
import heapq
from itertools import combinations
from collections import defaultdict


def sssp(graph, source):
    heap = []
    visited = set()
    distances = defaultdict(lambda: float("inf"))
    distances[source] = 0
    heapq.heappush(heap, (0, source))
    while len(heap) > 0:
        _, current = heapq.heappop(heap)
        for neighbor, weight in graph[current].items():
            if (
                neighbor not in visited
                and distances[neighbor] > distances[current] + weight
            ):
                visited.add(neighbor)
                distances[neighbor] = distances[current] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))
    return distances


def part1_solution(
    graph: Dict[Tuple[int, int], Dict[Tuple[int, int], float]],
    galaxies: Set[Tuple[int, int]],
):
    galaxy_distances = {galaxy: sssp(graph, galaxy) for galaxy in galaxies}
    return sum(
        galaxy_distances[galaxy1][galaxy2]
        for galaxy1, galaxy2 in combinations(galaxies, 2)
    )


if __name__ == "__main__":
    print(part1_solution(*parse_input("example.txt", 2)))
    print(part1_solution(*parse_input("input.txt", 2)))
    print(part1_solution(*parse_input("input.txt", 1_000_000)))
