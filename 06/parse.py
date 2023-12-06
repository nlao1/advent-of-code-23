from typing import List


def parse_input(filename):
    with open(filename) as f:
        times = f.readline()
        race_times = list(filter(lambda x: len(x) > 0, times.strip().split(" ")[1:]))
        distances = f.readline()
        race_distances = list(
            filter(lambda x: len(x) > 0, distances.strip().split(" ")[1:])
        )
        return list(zip(race_times, race_distances))
