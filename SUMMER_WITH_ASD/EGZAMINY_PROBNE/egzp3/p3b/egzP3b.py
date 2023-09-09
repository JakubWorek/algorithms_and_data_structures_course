from egzP3btesty import runtests 
from queue import PriorityQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def make_set(v):
    return Node(v)

def kruskal_algorithm(graph, edges):
    MST = []
    V = []
    for i in range(len(graph)):
        V.append(make_set(i))
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
    return MST

def lufthansa ( G ):
    output = 0

    E = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                output += G[i][j][1]
                E.append([i, G[i][j][0], G[i][j][1]])
    
    E.sort(key = lambda x: -x[2])
    mst = kruskal_algorithm(G, E)
    
    i = 0
    while i < len(mst):
        if E[i][2] == mst[i][2]: i+=1
        else: break
    
    j=i
    
    mst_w = 0
    for i in range(len(mst)):
        mst_w += mst[i][2]
    
    mst_w += E[j][2]

    return output - mst_w

runtests ( lufthansa, all_tests=True )