#!/usr/bin/env python3
from scipy.spatial.distance import cdist
import numpy as np
import tqdm
import re

# Part 1 is straightforward. However, we need to be smart for Part 2
# else we will exhaust our computer's resources (the searching space
# is 4000000² which will take 16Tb of memory if we want to allocate a
# buffer of this size, and take forever if we try to iterate over all
# points).
#
# So the trick is to reduce the search space. Because we know there is
# only 1 possible solution It has to be right next to the range
# detected by a sensor. So we will iterate over these points only:
# There are roughly 4*len(sensors)*mean(distances) ~ 100 million of
# these points.


h_lim = 20  # test data search space
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
h_lim = 4000000  # real data


# Parse all sensors and beacons positions from input
positions = [
    ((int(a[0]), int(a[1])), (int(a[2]), int(a[3])))
    for a in re.findall(
        r".*x=(\d+).*y=(\d+).*x=([-\d]+).*y=(\d+).*", test_data, re.MULTILINE
    )
]

# Convert everything to numpy
positions = np.array(positions)
sensors = positions[:, 0, :].astype(int)
beacons = positions[:, 1, :].astype(int)

# For each sensor, compute the distance to its beacon
# We use scipy.cdist here, which is able to work on arrays
#
# cdist will return a matrix of distances between all sensors and
# all beacons. Because we only care about the beacons heard for each
# sensor, we select only the diagonal from the resulting matrix
#
# Convert to integer type because default (float) uses more resources
# and can't be directly used as index
distances = np.diag(cdist(beacons, sensors, metric="cityblock")).astype(int)


def get_perimeter(distance):
    """Return the 'perimeter' around (0,0) for the given range in the
    manhattan distance.  ie: return an array of all points located at
    exactly 'distance + 1' from the center.

    :param distance: int Distance from the center
    :return array: numpy array of the contour. Length: 4*(distance+1)
    """
    # get the 2 corners separately
    corners = np.array([[0, distance + 1], [distance + 1, 0]])

    # One diagonal- without corners to avoid duplicates
    line = np.array(list(zip(range(1, distance), range(distance, 0, -1))))
    if len(line) > 0:
        # get the symetrical along x axis
        oline = np.multiply(line, [1, -1])

        # append everything with their symetrical along y axis
        return np.concatenate((line, -line, oline, -oline, corners, -corners), axis=0)
    else:
        return corners


# Now, for each sensor:
for i in tqdm.tqdm(range(len(sensors))):
    sensor, distance = sensors[i], distances[i]

    # Offset the perimeter to match the sensor center
    contour = get_perimeter(distance) + sensor
    # remove invalid values
    c_filt = contour[
        (contour[:, 0] <= h_lim)
        & (contour[:, 0] >= 0)
        & (contour[:, 1] <= h_lim)
        & (contour[:, 1] >= 0)
    ]

    # get distances of all contour points to all sensors
    distances_from_sensor = cdist(c_filt, sensors, metric="cityblock").astype(int)
    # check if a point is not in range of all sensors -> this is the
    # one we're looking for
    if np.any((distances_from_sensor > distances).all(1)):
        response = c_filt[(distances_from_sensor > distances).all(1)]
        print("Part 2: found potential position at ", response)
        print("\tSolution would be: ", response[0][0] * 4000000 + response[0][1])

# If all is correct, we only find 1 potential solution
print("The end")
