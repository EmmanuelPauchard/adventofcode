#!/usr/bin/env python3


class AdventOfCode:
    def __init__(self, input_data, name="") -> None:
        self.input_data = input_data
        self.name = name

    def run(self):
        print(f"Running AdventOfCode {self.name}: {self.solve()}")

    def solve(self):
        """
        Run the day challenge and return result
        """
        pass


def AdventOfCodeFromFileInput(advent_of_code_class, input_file) -> AdventOfCode:
    with open(input_file, "r") as f:
        input_data = f.read()
    return advent_of_code_class(input_data, advent_of_code_class.__name__)
