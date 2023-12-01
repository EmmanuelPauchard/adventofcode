#!/usr/bin/env python3

import re

test = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

challenge_1 = open("/home/epauchard/sandbox/aoc23/inputs/input_1.awav", "r").read()


inp = test
inp = challenge_1  #
# inp = test_2  #

m = r"(\d|one|two|three|four|five|six|seven|eight|nine)"

conv = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_number(line):
    first_dig = re.match(r"\w*?" + m, line).groups()[0]
    last_dig = re.match(r"\w*" + m, line).groups()[0]
    print("Analysing: ", line)
    print("Found: ", first_dig, last_dig)

    y = []
    for i in [first_dig, last_dig]:
        try:
            y += [int(i)]
        except ValueError:
            y += [conv[i]]
    print("This line is: ", y[0] * 10 + y[1])
    return y[0] * 10 + y[1]


print("Answer is: ", sum(map(get_number, inp.split())))
