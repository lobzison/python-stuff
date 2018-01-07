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
       returns a tuple of format (distance, (x1, y1), (x2, y2))
       takes O(N^2)"""
    min_dist = (float("inf"), (None, None), (None, None))
    for point1 in points_list:
        for point2 in points_list:
            new_dist = (e_distance(point1, point2), point1, point2)
            if new_dist[0] < min_dist[0] and point1 is not point2:
                min_dist = new_dist
    return min_dist


def divide_and_conquer(points_list):
    """
    Takes list of tuples of format (x, y) sorted in x ASC,
    returns a tuple of format (distance, (x1, y1), (x2, y2))
    takes O(N^2)"""
    # step 0
    num_points = len(points_list)
    if num_points <= 3:
        return brute_force(points_list)
    mid_index = num_points // 2
    left_result = divide_and_conquer(points_list[:mid_index])
    right_results = divide_and_conquer(points_list[mid_index:])
    result = min(left_result, (right_results[0],
                               (right_results[1][0] +
                                mid_index, right_results[1][1]),
                               (right_results[2][0] +
                                mid_index, right_results[2][1])))
    mid_strip_disrt = (points_list[mid_index - 1][0] +
                       points_list[mid_index][0]) / 2
    result = min(result, colsest_pair_middle(points_list,
                                             mid_strip_disrt,
                                             result[0]))
    # print result

    return result


def colsest_pair_middle(points_list, mid, half_width):
    """Finds cloasest pairs in middle"""
    # take only points in middle strip
    # sort in Y ASC
    # print points_list
    middle_points = [point for point in points_list
                     if abs(point[0] - mid) < half_width]
    middle_points.sort(key=lambda x: x[1])
    size = len(middle_points)
    result = (float("inf"), (None, None), (None, None))
    for point1_idx in range(size - 1):
        for point2_idx in range(point1_idx + 1,
                                min(point1_idx + 4, size)):
            dist = e_distance(middle_points[point1_idx],
                              middle_points[point2_idx])
            result = min(result, (dist,
                                  middle_points[point1_idx],
                                  middle_points[point2_idx]))
            # print result
    return result
