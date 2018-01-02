"""
Algorithms for finding shortest distance between set of points
"""

import math


def e_distance(point1, point2):
    """Calculates the euclidian distance betweeb two points"""
    return math.sqrt((point1[0] - point2[0]) ** 2 +
                     (point1[1] - point2[1]) ** 2)


def brute_force(points_list):
    """Takes list of tuples of format (x, y),
       returns a tuple of format (distance, (x1, y1), (x2, y2))"""
    min_dist = (float("inf"), (None, None), (None, None))
    for point1 in points_list:
        for point2 in points_list:
            new_dist = (e_distance(point1, point2), point1, point2)
            if new_dist[0] < min_dist[0]:
                min_dist = new_dist
    return min_dist
