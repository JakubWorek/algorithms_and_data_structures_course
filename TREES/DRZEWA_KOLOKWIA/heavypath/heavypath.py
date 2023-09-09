from zad1tests import Node, runtests

def relax(paths, length):
    if paths[0] < paths[1] and length > paths[0]: paths[0] = length
    elif length > paths[1]: paths[1] = length

def heavy_path(T):
    _max = 0

    def rec(node):
        # przechodzimy po wszystkich node-ach
        # i znajdujemy dwie (o ile istnieją) najdłuższe ścieżki
        max_path = [0,0]
        for child, weight in node.child:
            length = rec(child) + weight
            relax(max_path, length)

        curr = max(max_path)
        nonlocal _max
        _max = max(_max, curr, sum(max_path))

        return curr
    
    rec(T)
    return _max

runtests(heavy_path)