import numpy as np

# Calculate the angle between three points p1, p2, p3
# This function finds the angle at p2 formed by the lines joining p1-p2 and p2-p3.
# It uses the arctan2 function to compute the angles of these lines relative to the x-axis
# and then subtracts them. The result is converted from radians to degrees.
def get_angle(p1, p2, p3):
    rad = np.arctan2(p3[1] - p2[1], p3[0] - p2[0]) - np.arctan2(p1[1] - p2[1], p1[0] - p2[0])
    return abs(np.degrees(rad))

# Calculate the distance between two points
# This function computes the Euclidean distance between the first two points in the given list.
# If fewer than two points are provided, it returns None. The distance is scaled to a range of 0 to 1000.
def get_distance(coords):
    if len(coords) < 2:  # Ensure there are at least two points
        return
    (x1, y1), (x2, y2) = coords[0], coords[1]  # Unpack the coordinates of the first two points
    dist = np.hypot(x2 - x1, y2 - y1)  # Calculate the Euclidean distance
    return np.interp(dist, [0, 1], [0, 1000])  # Scale the distance to the range [0, 1000]
