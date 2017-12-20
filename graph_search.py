"""
Search graph, compute reilience
"""
from collections import deque
import random

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
        graph.pop(node)
        for edge in ugraph.values():
            if node in edge:
                edge.remove(node)
    graph = ugraph
    resilience = []
    for attack in attack_order:
        resilience.append(largest_cc_size(graph))
        remove_node(graph, attack)
    resilience.append(largest_cc_size(graph))
    return resilience


print compute_resilience(GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])
