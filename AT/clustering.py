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
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    result = (float("inf"), -1, -1)
    num_clusters = len(cluster_list)
    for cluster in range(num_clusters):
        for other_cluster in range(num_clusters):
            if cluster != other_cluster:
                dist_clust = pair_distance(cluster_list, cluster, other_cluster)
                result = min(result, dist_clust)
    return result


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    num_clusters = len(cluster_list)
    if num_clusters <= 3:
        return slow_closest_pair(cluster_list)
    middle = num_clusters // 2
    left_part = [cluster for cluster in cluster_list[:middle]]
    right_part = [cluster for cluster in cluster_list[middle:]]
    result_left = fast_closest_pair(left_part)
    result_right = fast_closest_pair(right_part)
    result = min(result_left, (result_right[0], result_right[1] + middle, result_right[2] + middle))
    mid = (cluster_list[middle - 1].horiz_center() + cluster_list[middle].horiz_center()) / 2
    result = min(result, closest_pair_strip(cluster_list, mid, result[0]))
    return result


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    center_area_clusters = [cluster for cluster in cluster_list 
                            if abs(cluster.horiz_center() - horiz_center) < half_width]
    center_area_clusters.sort(key = lambda cluster: cluster.vert_center())
    size = len(center_area_clusters)
    result = (float("inf"), -1, -1)
    for cluster_idx1 in range(size - 1):
        for cluster_idx2 in range(cluster_idx1 + 1, min(cluster_idx1 + 4, size)):
            dist_clust = pair_distance(center_area_clusters, cluster_idx1, cluster_idx2)
            result = min(result, (dist_clust[0], center_area_clusters[cluster_idx1].horiz_center(), center_area_clusters[cluster_idx2].horiz_center()))
    return result
#                                                   horiz_pos, vert_pos, population, risk
print closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0),
                          alg_cluster.Cluster(set([]), 0, 1, 1, 0),
                          alg_cluster.Cluster(set([]), 0, 2, 1, 0),
                          alg_cluster.Cluster(set([]), 0, 3, 1, 0)],
                         0.0, 1.0)

#closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 1.5, 1.0) expected one of the tuples in set([(1.0, 1, 2)]) but received (Exception: TypeError) "unsupported operand type(s) for -: 'instancemethod' and 'float'" at line 92, in closest_pair_strip
#closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 0, 1, 1, 0), alg_cluster.Cluster(set([]), 0, 2, 1, 0), alg_cluster.Cluster(set([]), 0, 3, 1, 0)], 0.0, 1.0) expected one of the tuples in set([(1.0, 2, 3), (1.0, 0, 1), (1.0, 1, 2)]) but received (1.0, 0, 0)
# fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)]) expected one of the tuples in set([(1.0, 1, 2), (1.0, 0, 1), (1.0, 2, 3)]) but received (Exception: TypeError) "'tuple' object does not support item assignment" at line 71, in fast_closest_pair
#print fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)])

#print slow_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)])



######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    
    return []


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
            
    return []

