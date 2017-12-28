"""
Functions to calculate order of attack on graph
"""
import urllib2
import random
import time
import math
import graph_search as gs
import graph_degees_calc as gdc

GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)


def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def fast_target_order(ugraph):
    """
    Compute attack order, return nodes in order
    """
    result_order = []
    num_nodes = len(ugraph.keys())
    degrees = [set([]) for _ in range(num_nodes)]
    for node in ugraph.keys():
        node_degree = len(ugraph[node])
        degrees[node_degree].add(node)
    for degree in range(num_nodes - 1, -1, -1):
        while degrees[degree] != set([]):
            elem = degrees[degree].pop()
            for neighbor in ugraph[elem]:
                n_degree = len(ugraph[neighbor])
                degrees[n_degree].remove(neighbor)
                degrees[n_degree - 1].add(neighbor)
            result_order.append(elem)
            delete_node(ugraph, elem)
    return result_order


#test_graph = gdc.make_upa_graph(1300, 5)


def time_run(fnk):
    """Times fnk on upa graph"""
    xval = []
    yval = []
    for n in range(10, 1000, 10):
        xval.append(n)
        graph = gdc.make_upa_graph(n, 5)
        c_time = time.time()
        fnk(graph)
        time_passed = time.time() - c_time
        yval.append(time_passed)
    return xval, yval


# normal_x, normal_y = time_run(targeted_order)
# fast_x, fast_y = time_run(fast_target_order)

# gs.legend_example2(("targeted_order", normal_y, normal_x, '-b'),
#                ("fast_target_order", fast_y, fast_x, '-r'))

#print(fast_target_order(test_graph))
# print graph_search.imported_graph[148]
