from zad1testy import runtests
from queue import PriorityQueue
from math import inf

def convert(G):
    n = len(G)
    GG = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v]: 
                GG[u].append([v, G[u][v]])

    return GG

def islands(G, A, B):
    G = convert(G)
    #print(G)
    n = len(G)
    # w[u][0] - z 1, [1] - z 5, [2] - z 8
    weights = [[inf]*3 for _ in range(n)]
    Q = PriorityQueue()

    Q.put((0,A,None,1))
    Q.put((0,A,None,5))
    Q.put((0,A,None,8))

    def edge(prev):
        if prev == 1: return 0
        if prev == 5: return 1
        return 2

    while not Q.empty():
        min_w, u, parent, prev = Q.get()

        if min_w < weights[u][edge(prev)]:
            weights[u][edge(prev)] = min_w

            for v, weight in G[u]:
                if weights[v][edge(weight)] == inf and prev != weight:
                    Q.put((weights[u][edge(prev)]+weight, v, u, weight))

    if min(weights[B]) == inf: return None
    return min(weights[B])

runtests( islands ) 
