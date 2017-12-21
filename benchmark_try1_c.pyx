import time

#takes int returns tuple
cdef tuple make_tree(int d):
    if d > 0:
        d -= 1
        return (make_tree(d), make_tree(d))
    return (None, None)

#takes tuple, returns int
cdef int check_tree(tuple node):
    if node[0] is None:
        return 1
    return 1 + check_tree(node[0]) + check_tree(node[1])

#takes tupe returns int
cdef int make_check(tuple itde):
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

    print('stretch tree of depth %d\t check: %d'%(
          stretch_depth, make_check((0, stretch_depth))))

    long_lived_tree = make_tree(max_depth)

    mmd = max_depth + min_depth
    for d in range(min_depth, stretch_depth, 2):
        i = 2 ** (mmd - d)
        cs = 0
        for argchunk in get_argchunks(i,d):
            cs += sum(chunkmap(make_check, argchunk))
        print('%d\t trees of depth %d\t check: %d'%(i, d, cs))

    print('long lived tree of depth %d\t check: %d'%(
          max_depth, check_tree(long_lived_tree)))
    
start = time.time()
main(13)
print time.time() - start
