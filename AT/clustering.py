"""
Student template code for Project 3
Student will implement five functions:
slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)
where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance
    between two clusters in a list
    Input: cluster_list is list of clusters,
    idx1 and idx2 are integer indices for two clusters
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]),
            min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)
    Input: cluster_list is the list of clusters
    Output: tuple of the form (dist, idx1, idx2)
    where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2]
    have minimum distance dist.
    """
    result = (float("inf"), -1, -1)
    num_clusters = len(cluster_list)
    for cluster in range(num_clusters):
        for other_cluster in range(num_clusters):
            if cluster != other_cluster:
                dist_clust = pair_distance(
                    cluster_list, cluster, other_cluster)
                result = min(result, dist_clust)
    return result


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)
    Input: cluster_list is list of clusters
    SORTED such that horizontal positions of their
    centers are in ascending order
    Output: tuple of the form (dist, idx1, idx2)
    where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2]
    have minimum distance dist.
    """
    num_clusters = len(cluster_list)
    if num_clusters <= 3:
        return slow_closest_pair(cluster_list)
    middle = num_clusters // 2
    left_part = [cluster for cluster in cluster_list[:middle]]
    right_part = [cluster for cluster in cluster_list[middle:]]
    result_left = fast_closest_pair(left_part)
    result_right = fast_closest_pair(right_part)
    result = min(
        result_left,
        (result_right[0], result_right[1] + middle, result_right[2] + middle))
    mid = (cluster_list[middle - 1].horiz_center() +
           cluster_list[middle].horiz_center()) / 2
    result = min(result, closest_pair_strip(cluster_list, mid, result[0]))
    return result


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip
    (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)
    Output: tuple of the form (dist, idx1, idx2)
    where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie
    in the strip and have minimum distance dist.
    """
    center_area_clusters = [cluster for cluster in cluster_list
                            if abs(cluster.horiz_center() -
                                   horiz_center) < half_width]
    center_area_clusters.sort(key=lambda cluster: cluster.vert_center())
    size = len(center_area_clusters)
    result = (float("inf"), -1, -1)
    for cluster_idx1 in range(size - 1):
        for cluster_idx2 in range(cluster_idx1 + 1,
                                  min(cluster_idx1 + 4, size)):
            orig_idx1 = cluster_list.index(center_area_clusters[cluster_idx1])
            orig_idx2 = cluster_list.index(center_area_clusters[cluster_idx2])
            dist_clust = pair_distance(cluster_list, orig_idx1, orig_idx2)
            result = min(result, dist_clust)
    return result


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    clusters = [cluster.copy() for cluster in cluster_list]
    while len(clusters) > num_clusters:
        clusters.sort(key=lambda cluster: cluster.horiz_center())
        closest = fast_closest_pair(clusters)
        clusters[closest[1]].merge_clusters(clusters[closest[2]])
        clusters.pop(closest[2])
    return clusters


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    Input: List of clusters, integers number of clusters
    and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    cluster_list.sort(key = lambda x: x.total_population())
    initial_clusters = len(cluster_list)
    cluster_centres = [(cluster.horiz_center(),
                        cluster.vert_center())
                       for cluster in cluster_list[initial_clusters - num_clusters:]]
    print "---------"
    print cluster_list[initial_clusters - num_clusters:]
    print "---------"
    for iter in range(num_iterations):
        new_clusters = [alg_cluster.Cluster(set([]), cent[0], cent[1], 0, 0)
                        for cent in cluster_centres]
        for init_clust in cluster_list:
            min_dist = float("inf")
            min_dist_pair = (min_dist, -1, -1)
            # find pair of cluster with minimum distance between them
            for clust_pair in ((init_clust.distance(new_cluster), new_cluster, init_clust)
                            for new_cluster in new_clusters):
                if clust_pair[0] < min_dist:
                    min_dist = clust_pair[0]
                    min_dist_pair = clust_pair
            # merge cluster to closest
            min_dist_pair[1].merge_clusters(min_dist_pair[2])
            cluster_centres = [(clust.horiz_center(), clust.vert_center())
                               for clust in new_clusters]
    return new_clusters
            
    

    return cluster_centres

print kmeans_clustering([alg_cluster.Cluster(set(["1"]), 3, 4, 10, 0),
                         alg_cluster.Cluster(set(["2"]), 5, 6, 10, 0),
                         alg_cluster.Cluster(set(["3"]), 0, 1, 10, 0),
                         alg_cluster.Cluster(set(["4"]), 1, 1, 10, 0)], 15, 1)
