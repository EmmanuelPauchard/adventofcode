#!/usr/bin/env python3
import re

test_data = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

# Comment the following 3 lines to use test data
with open("2022/15.in") as f:
    data = f.read()
test_data = data

def dist(s, b):
    return abs(b[1]-s[1]) + abs(b[0]-s[0])

positions = [((int(a[0]), int(a[1])), (int(a[2]), int(a[3]))) for a in re.findall(r'.*x=(\d+).*y=(\d+).*x=([-\d]+).*y=(\d+).*', test_data, re.MULTILINE)]
print("Positions: ", positions)

distances = [dist(b,s) for b,s in positions]
print("Distance: ", distances)

beacons = []
sensors = []
for s, b in positions:
    beacons += [b]
    sensors += [s]

print("Beacons:", beacons)
print("Sensors: ", sensors)


min_col = min([x[0] for x in beacons + sensors])
max_col = max([x[0] for x in beacons + sensors])
min_row = min([x[1] for x in beacons + sensors])
max_row = max([x[1] for x in beacons + sensors])

max_dist = max(distances)

count = []
start_row = 2000000
# start_row = 10  # test data

import tqdm

for start_col in tqdm.tqdm(range(min_col-max_dist, max_col+1+max_dist)):
    # print("Current position: ", (start_col, start_row))
    if (start_col, start_row) in sensors + beacons:
        # print("Already a beacon/sensor here")
        continue
    for point, d in zip(sensors, distances):
        s = dist(point, (start_col, start_row))
        # print(f"point {point} sensor distance {d}. Current {s}")
        if s <= d:
            count += [start_col]
            break

print(len(count))

# part 1: 4432197 too low
