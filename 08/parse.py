from typing import Dict, Tuple


def parse_input(filename):
    with open(filename) as f:
        direction_sequence = list(f.readline().strip())
        f.readline()
        network: Dict[str, Tuple[str, str]] = {}
        for line in f:
            node, instructions = line.strip().split(" = ")
            node = node.strip()
            instruction_l, instruction_r = instructions.strip().split(", ")
            # shave off (
            instruction_l = instruction_l[1:]
            # shave off )
            instruction_r = instruction_r[:-1]
            network[node] = (instruction_l, instruction_r)
        return direction_sequence, network
