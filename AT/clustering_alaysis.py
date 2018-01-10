"""Analysis of clustering algorythms"""

import clustering
import alg_cluster
import random
import time
import matplotlib.pyplot as plt
import math




def gen_random_clusters(num_clusters):
    """
    Generates a list of clusters in with center in square (+-1, +-1)
    """
    result = [alg_cluster.Cluster(0,
                                  random.random() * 2 - 1,
                                  random.random() * 2 - 1,
                                  0, 0)
              for _ in
              range(num_clusters)]
    return result


def time_run_brute(runs):
    """Times fnk on upa graph"""
    xval = []
    yval = []
    for n in range(2, runs):
        xval.append(n)
        test_list = gen_random_clusters(n)
        c_time = time.time()
        clustering.slow_closest_pair(test_list)
        time_passed = time.time() - c_time
        yval.append(time_passed)
    return [xval, yval]

def time_run_divide(runs):
    """Times fnk on upa graph"""
    xval = []
    yval = []
    for n in range(2, runs):
        xval.append(n)
        test_list = gen_random_clusters(n)
        #test_list.sort(key=lambda x: x.horiz_center())
        c_time = time.time()
        clustering.fast_closest_pair(test_list)
        time_passed = time.time() - c_time
        yval.append(time_passed)
    return [xval, yval]


def plot():
    runs = 200
    time_brute = time_run_brute(runs)
    time_divide = time_run_divide(runs)
    plt.plot(time_brute[0], time_brute[1], '-r', label="slow_closest_pair")
    plt.plot(time_divide[0], time_divide[1], '-g', label="fast_closest_pair")
    plt.xlabel("Number of clusters in set")
    plt.ylabel("Runtime")
    plt.title("Runtimes of fast and slow algorythms")
    plt.legend()
    plt.show()


def compute_distortion(cluster_list, data_table):
    """
    Given list of cluster, computes distortion of all clusters
    Returns a number of distortion
    """
    return sum((abs(cluster.cluster_error(data_table))
                for cluster in cluster_list))

# if __name__ == "__main__":
#     plot()