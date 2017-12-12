def union(set1, set2):
    """
    Returns the union of two sets.

    Arguments:
    set1 -- The first set of the union.
    set2 -- The second set of the union.

    Returns:
    A new set containing all the elements of set1 and set2.
    """
    res = set1.copy()
    for item in set2:
        res.add(item)
    return res
        
print union(set(), set())

def intersection(set1, set2):
    """
    Returns the intersection of two sets.

    Arguments:
    set1 -- The first set of the intersection.
    set2 -- The second set of the intersection.

    Returns:
    A new set containing only the elements common to set1 and set2.
    """
    res = set()
    for item in set1:
        if item in set2:
            res.add(item)
    return res

print intersection(set([1,2,3]), set([2,3,4]))
print intersection(set([1,2]), set([3,4]))
print intersection(set(), set([3]))

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

print make_dict(["a","b","c"], "z")
print make_dict([], [])

def ensure_key_value_pair(pairs, key, expected_value):
    """
    Checks to ensure that the mapping of key in pairs matches the given expected value.

    If the state of pairs is such that the given key is already mapped to the given expected value
    this function in no way modifies the dictionary and returns the given dictionary.

    If the state of pairs is such that the given key does not map to the given expected value
    (or no such key is contained in pairs) then update (or add) the mapping of key to
    the given expected value and return the given dictionary.

    Arguments:
    pairs          -- A dictionary to check for the expected mapping.
    key            -- The key of the expected mapping.
    expected_value -- The the value of the expected mapping.

    Returns:
    The given dictionary.
    """
    if pairs.has_key(key):
        if pairs[key] != expected_value:
            pairs[key] = expected_value
    else:
        pairs[key] = expected_value
    return pairs

pairs = { 1:"a", 2:"b" }
print ensure_key_value_pair(pairs, 1, "a")
print ensure_key_value_pair(pairs, 2, "z")
print ensure_key_value_pair(pairs, 3, "x")
    
