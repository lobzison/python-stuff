"""
Search graph, compute reilience
"""
from collections import deque
import random
import urllib2
import time
import math
import graph_degees_calc

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
        remove_node(graph, attack)
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

imported_graph = load_graph(NETWORK_URL)

#print compute_resilience(imported_graph,[1, 2, 3, 4, 5, 6, 7])


print graph_degees_calc.make_random_graph_undir(10, 0.9)
print graph_degees_calc.make_upa_graph(10, 3)


def random_order(graph):
    """
    Takes graph, returns nodes in random order
    """
    nodes = graph.keys()
    random.shuffle(nodes)
    return nodes


make_random_graph_undir(num_nodes, probablitiy):



print compute_resilience(imported_graph, random_order(imported_graph))

