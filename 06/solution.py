import parse


def solve(time_distance_pairs):
    result = 1
    for time, distance_needed in time_distance_pairs:
        time = int(time)
        distance_needed = int(distance_needed)
        num_ways_to_win = 0
        for speed in range(time):
            remaining_time = time - speed
            distance = remaining_time * speed
            if distance > distance_needed:
                num_ways_to_win += 1
        result *= num_ways_to_win
    return result


def part1_solution(filename):
    time_distance_pairs = parse.parse_input(filename)
    return solve(time_distance_pairs)
    # must travel {distance} in remaining_time/time


def part2_solution(filename):
    time_distance_pairs = parse.parse_input(filename)
    real_time = ""
    real_distance = ""
    for time, distance in time_distance_pairs:
        real_time += time
        real_distance += distance
    real_time = int(real_time)
    real_distance = int(real_distance)
    return solve([(real_time, real_distance)])


if __name__ == "__main__":
    print(part1_solution("example.txt"))
    print(part1_solution("input.txt"))
    print(part2_solution("example.txt"))
    print(part2_solution("input.txt"))
