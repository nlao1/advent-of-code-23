from typing import List, Tuple


def parse_input(filename) -> List[Tuple[int, List[Tuple[int, int, int]]]]:
    with open(filename) as f:
        games = []
        for line in f:
            line = line.strip()
            game_str, sets_str = line.split(":")
            sets = sets_str.split(";")
            game_num = int(game_str.split(" ")[1])
            sets_in_game = []
            for set in sets:
                revealed_cubes = set.split(",")
                red = 0
                green = 0
                blue = 0
                for cube in revealed_cubes:
                    cube = cube.strip()
                    if cube.endswith("red"):
                        red = int(cube.split(" ")[0])
                    elif cube.endswith("green"):
                        green = int(cube.split(" ")[0])
                    elif cube.endswith("blue"):
                        blue = int(cube.split(" ")[0])
                sets_in_game.append((red, green, blue))
            games.append((game_num, sets_in_game))
        return games
