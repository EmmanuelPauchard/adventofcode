#!/usr/bin/env python3
import numpy as np
import itertools

test_data = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

lines = test_data.strip().split("\n")

# Comment the following 3 lines to use test data
with open("2022/14.in") as f:
    data = f.read()
lines = data.strip().split("\n")


# Create a 2D array of the cave where each pixel is 1 if path is
# blocked, 0 otherwise

world = np.zeros((1000, 1000), dtype=int)


def get_int(a, b):
    x = min(a, b)
    y = max(a, b)
    return (x, y)


deepest_level = 0
for line in lines:
    points = [(int(a.split(",")[0]), int(a.split(",")[1])) for a in line.split(" -> ")]
    for pt1, pt2 in zip(points[:-1], points[1:]):
        # Draw points
        world[pt1] = 1
        world[pt2] = 1
        if pt1[0] == pt2[0]:
            # Draw Vertical line
            x, y = get_int(pt1[1], pt2[1])
            world[pt1[0], x:y] = 1
        if pt1[1] == pt2[1]:
            # Draw Horizontal line
            x, y = get_int(pt1[0], pt2[0])
            world[x:y, pt1[1]] = 1

        if pt1[1] > deepest_level:
            deepest_level = pt1[1]

        if pt2[1] > deepest_level:
            deepest_level = pt2[1]

# Starting point
world[500, 0] = 0

sand_units = 0

for step in (1, 2):
    if step == 2:
        print("Setting deepest level to ", deepest_level + 2)
        world[:, deepest_level + 2] = 1
        deepest_level += 2

    while True:
        sand_units += 1
        cur_x = 500
        max_y = 0

        while True:
            if world[cur_x, max_y + 1] == 0:
                max_y += 1
                if max_y > deepest_level:
                    break
            else:
                if world[cur_x - 1, max_y + 1] == 0:
                    max_y += 1
                    cur_x -= 1
                elif world[cur_x + 1, max_y + 1] == 0:
                    max_y += 1
                    cur_x += 1
                else:
                    # stop
                    world[cur_x, max_y] = 1
                    break

        # remove 1 because the maximum was reached one step before
        if max_y > deepest_level:
            print("Step 1: Endless void is reached after ", sand_units - 1)
            break

        if max_y == 0 and sand_units >= 1:
            print("Step 2: Top is reached at ", sand_units - 1)
            break

# Show the world map
# with np.printoptions(threshold=sys.maxsize, linewidth=500):
#     print(world[485:505, 0:20].T)
