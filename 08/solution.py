import parse
from typing import List
from math import lcm


def part1_solution(filename):
    num_steps = 0
    direction_sequence, network = parse.parse_input(filename)

    def get_direction_of_step(idx):
        return direction_sequence[idx % len(direction_sequence)]

    direction_idx = 0
    curr_node = "AAA"
    while curr_node != "ZZZ":
        tuple_idx = 1 if get_direction_of_step(direction_idx) == "R" else 0
        curr_node = network[curr_node][tuple_idx]
        num_steps += 1
        direction_idx += 1
    return num_steps


def part2_solution(filename):
    num_steps = 0
    direction_sequence, network = parse.parse_input(filename)

    def get_direction_of_step(idx):
        return direction_sequence[idx % len(direction_sequence)]

    direction_idx = 0
    nodes = list(filter(lambda x: x.endswith("A"), network.keys()))
    num_steps_before_z = [0 for _ in nodes]
    z_cycle_length = [0 for _ in nodes]
    while num_steps < 60000:
        tuple_idx = 1 if get_direction_of_step(direction_idx) == "R" else 0
        if all(z > 0 for z in z_cycle_length):
            break
        for i, node in enumerate(nodes):
            # store position in the direction sequence
            if node.endswith("Z"):
                if num_steps_before_z[i] == 0:
                    num_steps_before_z[i] = num_steps
                elif num_steps_before_z[i] != 0:
                    z_cycle_length[i] = num_steps - num_steps_before_z[i]
            new_node = network[node][tuple_idx]
            nodes[i] = new_node
        num_steps += 1
        direction_idx += 1
    return lcm(*num_steps_before_z)


if __name__ == "__main__":
    print(part1_solution("example1.txt"))
    print(part1_solution("example2.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example3.txt"))
    print(part2_solution("input.txt"))
