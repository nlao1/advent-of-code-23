from typing import List, Tuple, Dict


def parse_input(filename):
    with open(filename) as f:
        # parse every number and the location of every symbol
        coord_to_data: Dict[Tuple[int, int], Tuple[int, int]] = {}
        symbol_indices: List[Tuple[Tuple[int, int], str]] = []
        for line_num, line in enumerate(f):
            line = line.strip()
            running = []

            def process_number():
                num_digits = len(running)
                for i in range(num_digits):
                    coord_to_data[(line_num, line_idx - i - 1)] = (
                        int("".join(running)),
                        num_digits - i - 1,
                    )

            for line_idx, c in enumerate(line):
                if c.isnumeric():
                    running.append(c)
                else:
                    if c != ".":
                        symbol_indices.append(((line_num, line_idx), c))
                    process_number()
                    # reset
                    running = []
            if len(running) > 0:
                process_number()

        return coord_to_data, symbol_indices
