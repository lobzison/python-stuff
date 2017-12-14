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
