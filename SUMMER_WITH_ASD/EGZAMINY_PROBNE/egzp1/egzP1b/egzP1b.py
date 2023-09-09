from egzP1btesty import runtests
from math import inf
from queue import PriorityQueue

def turysta( G: 'graph given by edges list', D: 'train', L: 'plane' ) -> int:
    #konstrukcja grafu
    n = 0
    for u, v, _ in G:
        n = max(u, v, n)
    n+=1

    GG = [[] for _ in range(n)]
    for u, v, w in G:
        GG[u].append((v,w))
        GG[v].append((u,w))

    # algorytm dijkstry
    weight = [[inf for _ in range(5)] for __ in range(n)]
    visited = [[False for _ in range(5)] for _ in range(n)]
    weight[D][0] = 0
    Q = PriorityQueue()
    Q.put((0,1,D))

    while not Q.empty():
        distance, ind, u = Q.get()
        if ind < 5:
            for v, time in GG[u]:
                if not visited[v][ind]\
                    and weight[v][ind] > distance + time:
                    weight[v][ind] = distance + time
                    Q.put((distance+time, ind+1, v))
            visited[u][ind - 1] = True

    return weight[L][4]

runtests ( turysta )