from typing import List


def parse_input(filename):
    histories = []
    with open(filename) as f:
        for line in f:
            histories.append(list(map(int, line.strip().split())))
        return histories
