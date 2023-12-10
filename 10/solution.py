import parse
from typing import Tuple, List, Dict
from collections import defaultdict, deque


def keep_undirected_edges_of_graph(
    graph: Dict[Tuple[int, int], List[Tuple[int, int]]]
) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    new_graph = {k: [] for k in graph}
    for node in graph:
        for neighbor in graph[node]:
            if node in graph[neighbor]:
                new_graph[node].append(neighbor)
    return new_graph


def part1_solution(filename):
    animal_position, graph = parse.parse_input(filename)
    graph = keep_undirected_edges_of_graph(graph)
    discovered = set()
    distance: Dict[Tuple[int, int], int] = {}
    distance[animal_position] = 0
    queue = deque([animal_position])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in discovered:
                discovered.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return max(distance.values())


def part2_solution(filename):
    pass


if __name__ == "__main__":
    print(part1_solution("simple_animal_example.txt"))
    print(part1_solution("simple_animal_example_extra.txt"))
    print(part1_solution("complex_example.txt"))
    print(part1_solution("complex_example_extra.txt"))
    print(part1_solution("input.txt"))
