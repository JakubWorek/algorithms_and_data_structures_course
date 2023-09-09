from egz1btesty import runtests
from math import inf
from queue import PriorityQueue

def create_graph(D, C, T, E):
    roz = len(D)
    n = roz * (E+1)

    GG = [[-1] * n for _ in range(n)]
    GG[0][0] = 0

    for i in range(1,roz):
        distance = D[i] - D[i-1]
        for j in range(distance, E+1):
            GG[(i-1)*(E+1) + j][i*(E+1) + j - distance ] = 0

    for i in range(roz):
        for j in range(E):
            GG[i*(E+1) + j][i*(E+1) + j+1] = C[i]

    for i in range(roz):
        if i != T[i][0]:
            GG[i*(E+1)][T[i][0]*(E+1)] = T[i][1]

    return GG

def dijkstra(G, s, t):
    n = len(G)
    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0
    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        u = q.get()[1]
        for v in range(n):
            if G[u][v] != -1 and dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
                parent[v] = u
                q.put((dist[v], v))

    return dist[t]

def planets( D, C, T, E ):
    G = create_graph(D, C, T, E)
    roz = len(D)
    sol = dijkstra(G, 0, ((roz-1)*(E+1))+1)
    return sol

runtests( planets, all_tests = True )