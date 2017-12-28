"""
Search graph, compute reilience
"""
from collections import deque
import random
import urllib2
import time
import math
import graph_degees_calc
import matplotlib.pyplot as plt
import copy

GRAPH0 = {0: set([1]),
          1: set([0, 2]),
          2: set([1, 3]),
          3: set([2])}

GRAPH3 = {0: set([]),
          1: set([2]),
          2: set([1]),
          3: set([4]),
          4: set([3])}

GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}


def bfs_visited(ugraph, start_node):
    """
    Returns all reacheble nodes of ugraph from start_node
    """
    neighbours = deque()
    visited = set([start_node])
    neighbours.append(start_node)
    while neighbours:
        current_node = neighbours.popleft()
        for neighbour_node in ugraph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                neighbours.append(neighbour_node)
    return visited


def cc_visited(ugraph):
    """
    Returns set of connected components of graph
    """
    remaining_nodes = ugraph.keys()
    connected_set = []
    while remaining_nodes:
        random_node = random.choice(remaining_nodes)
        visited_nodes = bfs_visited(ugraph, random_node)
        connected_set.append(visited_nodes)
        remaining_nodes = [node for node in remaining_nodes
                           if node not in visited_nodes]
    return connected_set


def largest_cc_size(ugraph):
    """
    Returns size of the largest connected coponent
    """
    return 0 if not ugraph else max((len(neighbours)
                                     for neighbours in cc_visited(ugraph)))


def compute_resilience(ugraph, attack_order):
    """
    Returns list of largest components in graph,
    after removing the nodes in order of attack_order
    """
    def remove_node(ugraph, node):
        """
        Mutates graph removing node, and connected edges
        """
        neighbours = ugraph[node]
        graph.pop(node)
        for edge in neighbours:
            ugraph[edge].remove(node)
    graph = ugraph
    resilience = []
    for attack in attack_order:
        resilience.append(largest_cc_size(graph))
        delete_node(graph, attack)
    resilience.append(largest_cc_size(graph))
    return resilience


NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def random_order(graph):
    """
    Takes graph, returns nodes in random order
    """
    nodes = graph.keys()
    random.shuffle(nodes)
    return nodes


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


def fast_target_order(ugraph):
    """
    Compute attack order, return nodes in order
    """
    ugraph_c = copy.deepcopy(ugraph)
    result_order = []
    num_nodes = len(ugraph_c.keys())
    degrees = [set([]) for _ in range(num_nodes)]
    for node in ugraph_c.keys():
        node_degree = len(ugraph_c[node])
        degrees[node_degree].add(node)
    for degree in range(num_nodes - 1, -1, -1):
        while degrees[degree] != set([]):
            elem = degrees[degree].pop()
            for neighbor in ugraph_c[elem]:
                n_degree = len(ugraph_c[neighbor])
                degrees[n_degree].remove(neighbor)
                degrees[n_degree - 1].add(neighbor)
            result_order.append(elem)
            delete_node(ugraph_c, elem)
    return result_order

# print("--------")
imported_graph = load_graph(NETWORK_URL)
random_graph = graph_degees_calc.make_random_graph_undir(1239, 0.004)
upa_graph = graph_degees_calc.make_upa_graph(1239, 3)


imported_graph_nc = range(len(imported_graph.keys()) + 1)
random_graph_nc = range(len(random_graph.keys()) + 1)
upa_graph_nc = range(len(upa_graph.keys()) + 1)

imported_graph_rs = compute_resilience(imported_graph, fast_target_order(imported_graph))
random_graph_rs = compute_resilience(random_graph, fast_target_order(random_graph))
upa_graph_rs = compute_resilience(upa_graph, fast_target_order(upa_graph))

# print compute_resilience(imported_graph,[1, 2, 3, 4, 5, 6, 7])

# print graph_degees_calc.edge_count(imported_graph)
print graph_degees_calc.edge_count(graph_degees_calc.make_random_graph_undir(1239, 0.0039))
# print graph_degees_calc.edge_count(graph_degees_calc.make_upa_graph(1239, 3))


def legend_example(*args):
    """
    Plot multiple lines on one plot
    """
    for item in args:
        plt.plot(item[2], item[1], item[3], label=item[0])
    plt.legend(loc='upper right')
    plt.xlabel("Number of nodes removed")
    plt.ylabel("Largest connected component")
    plt.title("Comparison of resilience of graphs")
    plt.show()

def legend_example2(*args):
    """
    Plot multiple lines on one plot
    """
    for item in args:
        plt.plot(item[2], item[1], item[3], label=item[0])
    plt.legend(loc='upper right')
    plt.xlabel("Number of nodes in GPA graph(m = 5)")
    plt.ylabel("Time passed in ms")
    plt.title("Running time of fast vs normal target order algorithms - Desktop Python")
    plt.show()



legend_example(("Computer network graph", imported_graph_rs, imported_graph_nc, '-b'),
               ("ER graph(p = 0.004)", random_graph_rs, random_graph_nc, '-r'),
               ("UPA graph(m = 3)", upa_graph_rs, upa_graph_nc, '-g'))


# print compute_resilience(imported_graph, random_order(imported_graph))
