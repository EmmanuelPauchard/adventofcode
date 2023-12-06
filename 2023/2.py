#!/usr/bin/env python3

import math
import re

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


input_data = test_data
# real_data = open("/home/epauchard/perso/adventofcode/2023/input_2.awav", "r").read()
# input_data = real_data
input_sums = {"red": 12, "blue": 14, "green": 13}


def part1():
    possible = 0
    for i, line in enumerate(input_data.splitlines(), start=1):
        impossible = False
        for count, color in re.findall(r"(\d+) (\w+)", line):
            if int(count) > input_sums[color]:
                print(f"Impossible: {line}")
                print(f"{color} {count}")
                impossible = True
                break

        if not impossible:
            print(f"Possible: {line} (index {i})")
            possible += i

    print(f"Solution to part 1: {possible}")


def part2():
    result = 0
    for i, line in enumerate(input_data.splitlines(), start=1):
        game_set = {k: 0 for k in input_sums.keys()}
        for color in input_sums.keys():
            try:
                game_set[color] = max(
                    [int(v) for v in re.findall(f"(\d+) {color}", line)]
                )
            except ValueError:
                game_set[color] = 0
        print(f"Line {line}")
        print(f"Min set: {game_set}")
        print(f"Prod: {math.prod(game_set.values())}")
        result += math.prod(game_set.values())

    print("Solution to part2: ", result)


part1()
part2()
