"""
Breath first search of a graph
"""


class Queue():
    """Data structure queue"""

    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

    def enque(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)


def calc_distance(graph, node):
    """
    Takes a graph and a node
    returns distnace from a node to all other nodes
    """
    distance = {}
    for key in graph.keys():
        distance[key] = float("inf")
    neighbours = Queue()
    neighbours.enque(node)
    distance[node] = 0
    while len(neighbours) != 0:
        print neighbours
        current_node = neighbours.dequeue()
        for neighbour in graph[current_node]:
            if distance[neighbour] == float("inf"):
                neighbours.enque(neighbour)
                distance[neighbour] = distance[current_node] + 1
    return distance


graph = {0: set([1, 2]), 1: set([0, 3]), 2: set([0]),
         3: set([1, 4]), 4: set([3])}


print calc_distance(graph, 0)
