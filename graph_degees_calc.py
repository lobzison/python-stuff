"""
Simple graph distionary representation and calculation
"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]),
             3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
             3: set([7]), 4: set([1]), 5: set([2]), 6: set([]),
             7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    """
    Makes a dictionary representation of a full
    graph with num_nodes nodes
    returns dictionary representation
    """
    res = {}
    if num_nodes > 0:
        set_all_nodes = set(range(num_nodes))
        for node in range(num_nodes):
            ajasent_nodes = set_all_nodes.copy()
            ajasent_nodes.remove(node)
            res[node] = ajasent_nodes
    return res

def compute_in_degrees(digraph):
    """
    Computes in-degree of grapgh nodes
    digraph is directional graph represented as dict
    returns new dictionary with keys as nodes
    and values as in-degree
    """
    def make_dict(keys, default_value):
        """
        Creates a new dictionary with the specified keys and default value.
        Arguments:
        keys          -- A list of keys to be included in the returned dictionary.
        default_value -- The initial mapping value for each key.
        Returns:
        A dictionary where every key is mapped to the given default_value.
        """
        res ={}
        for key in keys:
            res[key] = default_value
        return res
    
    res = make_dict(digraph.keys(), 0)
    for node_out in digraph:
        for node_in in digraph[node_out]:
            res[node_in] += 1
    return res

def compute_in_degrees_old(digraph):
    """
    Computes in-degree of grapgh nodes
    digraph is directional graph represented as dict
    returns new dictionary with keys as nodes
    and values as in-degree
    """
    res = {}
    if digraph:
        for node_in in digraph:
            in_degree = 0
            for node in digraph:
                if node_in in digraph[node]:
                    in_degree += 1
            res[node_in] = in_degree
    return res

def in_degree_distribution(digraph):
    """
    Computes in-degree distribution of a graph
    returns dicitonary where keys are in-degrees
    and values are number of occurences
    """
    in_degree = compute_in_degrees(digraph)
    res = {}
    for node in in_degree:
        if in_degree[node] not in res:
            res[in_degree[node]] = 1
        else:
            res[in_degree[node]] += 1
    return res

def node_count(graph):
    """
    Returns the number of nodes in a graph.

    Arguments:
    graph -- The given graph.

    Returns:
    The number of nodes in the given graph.
    """
    return len(graph.keys())

print node_count(EX_GRAPH0)
print node_count(EX_GRAPH1)
print node_count(EX_GRAPH2)
print node_count({})
print "----------------"

def edge_count(graph):
    """
    Returns the number of edges in a graph.

    Arguments:
    graph -- The given graph.

    Returns:
    The number of edges in the given graph.
    """
    res = 0
    for edges in graph.values():
        res += len(edges)
    return res / 2

graph1 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1","0"]) }
print edge_count(graph1)
print edge_count(EX_GRAPH0)
print edge_count(EX_GRAPH1)
print edge_count(EX_GRAPH2)
print edge_count({})


 
    
def make_graph1(num_nodes):
    """
    #V = {0, 1, 2, 3, 4, 5} where an edge exists 
    from n to n+1 (for n = 0...4).
    Also include the edge (5,0)
    """
    res = {}
    for node in range(num_nodes + 1):
        res[node] = set([num for num in range(node, num_nodes + 1)
                         if num != node])
    res[num_nodes] = set([0])
    return res

def make_graph2(num_nodes):
    """
    #V = {0, 1, 2, 3, 4, 5} where an edge exists 
    from n to n+1 (for n = 0...4).
    Also include the edge (5,0)
    """
    res = {}
    for node in range(num_nodes + 1):
        res[node] = set([(node + 1) % (num_nodes + 1)])
    return res

print make_graph1(5)
print make_graph2(5)

def is_undirected_graph_valid(graph):
    """
    Tests whether the given graph is logically valid.

    Asserts for every unordered pair of distinct nodes {n1, n2} that
    if n2 appears in n1's adjacency set then n1 also appears in
    n2's adjacency set.  Also asserts that no node appears in 
    its own adjacency set and that every value that appears in
    an adjacency set is a node in the graph.

    Arguments:
    graph -- The graph in dictionary form to test.

    Returns:
    True if the graph is logically valid.  False otherwise.
    """
    for node in graph:
        for edge in graph[node]:
            if (edge not in graph) or (edge == node) or (node not in graph[edge]):
                return False
    return True

graph1 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1","0"]) }
print is_undirected_graph_valid(graph1)

graph2 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1"]) }
print is_undirected_graph_valid(graph2)

graph3 = make_complete_graph(100)
print is_undirected_graph_valid(graph3)

graph4 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1","3"]) }
print is_undirected_graph_valid(graph4)

graph5 = { "0" : set(["0"]) }


def find_popular_nodes(graph):
    avg_degree = (edge_count(graph) * 2) / node_count(graph)
    count = 0
    res = set([])
    for node in graph:
        if len(graph[node]) > avg_degree:
            res.add(node)
            count += 1
    return count, res

import urllib2
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/random10000.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
