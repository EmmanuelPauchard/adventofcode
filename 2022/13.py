#!/usr/bin/env python3

# In today's challenge we must compare some data according to the
# given rules.
#
# Despite its seemingly straightforward appearance I found this
# challenge really tricky.  My first attempts used a class to define
# the Message type and overloaded the comparison operator. But my
# implementation failed to properly handle the equality condition of
# items, and it took me a lot of time to understand it and implement
# it properly.
#
# Eventually, I found it easier in this exercise to use a procedural
# approach that kept very close to the text description of the rules.

# Part 2 was way easier in my opinion because you just need to use the
# comparison function defined in part 1 in a sorting algorithm.

test_data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
lines = test_data.strip().split("\n")

# Comment the following 3 lines to use test data
with open("13.in") as f:
    data = f.read()
lines = data.strip().split("\n")

# Break data into pairs
pairs = [(eval(lines[i]), eval(lines[i + 1])) for i in range(0, len(lines), 3)]

# Basic structure:
# message : [items]
# item: int || [item,...]

# All comparison functions will use the standard convention:
# return 0 => right == left
# return 1 => right > left
# return -1 => right < left
def compare_integers(l, r):
    if l == r:
        return 0
    else:
        if l < r:
            return -1
        else:
            return 1


def compare_list_to_list(l, r):
    for left, right in zip(l, r):
        # compare values
        if isinstance(left, list) and isinstance(right, list):
            res = compare_list_to_list(left, right)
        elif isinstance(left, list) and isinstance(right, int):
            res = compare_list_to_integer(left, right)
        elif isinstance(left, int) and isinstance(right, list):
            res = compare_integer_to_list(left, right)
        elif isinstance(left, int) and isinstance(right, int):
            res = compare_integers(left, right)
        else:
            raise AttributeError("Unknown case")

        if res == 0:
            continue
        else:
            # We can stop comparing here, we have a result
            return res

    # check if we have equality or one side ran out of items
    if len(l) == len(r):
        return 0
    elif len(l) < len(r):
        # Left ran out of items
        return -1
    else:
        # Right ran out of items
        return 1


def compare_list_to_integer(l, r):
    return compare_list_to_list(l, [r])


def compare_integer_to_list(l, r):
    return compare_list_to_list([l], r)


correct_order = [
    i for i, (l, r) in enumerate(pairs, 1) if compare_list_to_list(l, r) == -1
]

print(
    "Part 1: Sum of correct pairs indices: ",
    sum(correct_order),
)

# Part 2 - Now we must actually sort.
from functools import cmp_to_key
import math

# Store all markers here
markers = [[[2]], [[6]]]

# Unpack
messages = [e for p in pairs for e in p] + markers

# Sort and get result
orderer_msg = sorted(messages, key=cmp_to_key(compare_list_to_list))
print("Part 2: Result is: ", math.prod([orderer_msg.index(m) + 1 for m in markers]))
