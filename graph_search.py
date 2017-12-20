"""
Search graph, compute reilience
"""
from collections import deque

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
             3: set([7]), 4: set([1]), 5: set([2]), 6: set([]),
             7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}


def bsf_visited(ugraph, start_node):
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

print bsf_visited(EX_GRAPH2, 8)