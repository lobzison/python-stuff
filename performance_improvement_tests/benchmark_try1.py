

# takes int returns tuple
def make_tree(d):
    if d > 0:
        d -= 1
        return (make_tree2(d), make_tree2(d))
    return (None, None)

# takes tuple, returns int
def make_tree2(d):
    return (make_tree(d), make_tree(d)) 


def check_tree(node):
    if node[0] is None:
        return 1
    return 1 + check_tree2(node[0]) + check_tree2(node[1])

def check_tree2(node):
    return 1 + check_tree(node[0]) + check_tree(node[1])


# takes tupe returns int
def make_check(itde):
    d = itde[1]
    return check_tree(make_tree(d))



def get_argchunks(i, d, chunksize=5000):
    assert chunksize % 2 == 0
    chunk = []
    for k in range(1, i + 1):
        chunk.extend([(k, d)])
        if len(chunk) == chunksize:
            yield chunk
            chunk = []
    if len(chunk) > 0:
        yield chunk



def main(n, min_depth=4):

    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1
    chunkmap = map

    print('stretch tree of depth {0}\t check: {1}'.format(
          stretch_depth, make_check((0, stretch_depth))))

    long_lived_tree = make_tree(max_depth)

    mmd = max_depth + min_depth
    for d in range(min_depth, stretch_depth, 2):
        i = 2 ** (mmd - d)
        cs = 0
        for argchunk in get_argchunks(i, d):
            cs += sum(chunkmap(make_check, argchunk))
        print('{0}\t trees of depth {1}\t check: {2}'.format(i, d, cs))

    print('long lived tree of depth {0}\t check: {1}'.format(
          max_depth, check_tree(long_lived_tree)))

