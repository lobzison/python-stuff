import clustering
import alg_cluster
import imp

foo = imp.load_source('poc_simpletest', '../PoC/poc_simpletest.py')
foo.TestSuite()


#                                   horiz_pos, vert_pos, population, risk
print clustering.closest_pair_strip([alg_cluster.Cluster(set([]), 1.0, 1.0, 1, 0),
                                     alg_cluster.Cluster(
                                         set([]), 1.0, 5.0, 1, 0),
                                     alg_cluster.Cluster(
                                         set([]), 1.0, 4.0, 1, 0),
                                     alg_cluster.Cluster(set([]), 1.0, 7.0, 1, 0)],
                                    1.0, 3.0)

# closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 0, 1, 1, 0), alg_cluster.Cluster(set([]), 0, 2, 1, 0), alg_cluster.Cluster(set([]), 0, 3, 1, 0)], 0.0, 1.0) expected one of the tuples in set([(1.0, 2, 3), (1.0, 0, 1), (1.0, 1, 2)]) but received (1.0, 0, 0)
# fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)]) expected one of the tuples in set([(1.0, 1, 2), (1.0, 0, 1), (1.0, 2, 3)]) but received (Exception: TypeError) "'tuple' object does not support item assignment" at line 71, in fast_closest_pair
# print fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)])

# print slow_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0)])

print clustering.hierarchical_clustering([alg_cluster.Cluster(set([]), 1.0, 1.0, 1, 0),
                                          alg_cluster.Cluster(
                                              set([]), 1.0, 5.0, 1, 0),
                                          alg_cluster.Cluster(
                                              set([]), 1.0, 4.0, 1, 0),
                                          alg_cluster.Cluster(set([]), 1.0, 7.0, 1, 0)], 2)
