"""
Building b-tree in-memory
"""

class Node:
    """
    Node of the tree
    """
    def __init__(self, knuth_order):
        self._is_leaf = True
        self._t = knuth_order
        self._keys = []
        self._children = []

    @property
    def is_leaf(self):
        """If node is leaf return true, othervise - return false"""
        return self._is_leaf

    def add_key(self, key):
        """Adds key to the keys"""
        self._keys.append(key)
        self._keys.sort()

    def is_full(self):
        """Returns True if node is full"""
        return len(self._keys) >= 2 * self._t - 1
            
    

my_node = Node(3)
for num in range(10):
    my_node.add_key(num)
print(my_node._keys)
