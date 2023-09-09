from zad4_tests import runtests
from math import inf
from queue import Queue

def floyd_warshall(G):
    n = len(G)
    D = [[inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = 0
            elif G[i][j] != 0:
                D[i][j] = G[i][j]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
    return D

def bfs(G, s):
    n = len(G)
    visited = [False] * n
    visited[s] = True
    parents = [None] * len(G)

    queue = Queue()
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(n):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                parents[v] = u
                queue.put(v)

    return parents, visited

def print_solution(distance):
    for i in range(len(distance)):
        print(distance[i])

def transport_plutonu(G, A, B, d):
    n = len(G)
    m = n * n
    M = [[0 for _ in range(m)] for __ in range(m)]
    D = floyd_warshall(G)
    #print_solution(D)

    for i in range(n):
        for j in range(n):
            if i != j or D[i][j] > d:
                for u in range(n):
                    for v in range(n):
                        if D[u][v] < d or (u == j and v == i):
                            continue
                        if (j == v and G[i][u] != 0) or\
                            (i == u and G[j][v] != 0) or\
                            (G[i][u] != 0 and G[j][v] != 0):
                            M[i*n + j][u*n + v] = 1
    
    #print_solution(M)

    P, V= bfs(M,A*n + B)
    #if V[B*n + A]: return True
    #return False
    R = []
    i = B*n + A
    while i is not None:
        R.append((i//n, i%n))
        i = P[i]
    R.reverse()
    return R

graph = [
    [0,3,4,4],
    [3,0,7,2],
    [4,7,0,5],
    [4,2,5,0]
]

graph1 = [
    [0,10,7,8,9],
    [10,0,2,6,3],
    [7,2,0,5,11],
    [8,6,5,0,3],
    [9,3,11,3,0]
]


#print(transport_plutonu(graph1,1,3,3))
runtests(transport_plutonu)