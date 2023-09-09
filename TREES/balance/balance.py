from zad2testy import runtests
from math import inf

class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.sums = 0

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)


def sums(root):
    for i in range(len(root.edges)):
        sums(root.edges[i])
        root.sums += root.edges[i].sums + root.weights[i]

def find(root):
    res = -1
    minDiff = inf

    def rec(node):
        nonlocal res, root, minDiff
        for i in range(len(node.edges)):
            _min = abs(2*node.edges[i].sums - root.sums + node.weights[i])
            if minDiff > _min:
                res = node.ids[i]
                minDiff = _min
                rec(node.edges[i])
    
    rec(root)
    return res


def balance( T ):
    """tu prosze wpisac wlasna implementacje"""
    sums(T)
    return find(T)

    
runtests( balance )


