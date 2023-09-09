from zad3testy import runtests
from zad3EK    import edmonds_karp
from math import inf

def floyd_warshall(graph):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance

def BlueAndGreen(T, K, D):
    # tu prosze wpisac wlasna implementacje
    T = floyd_warshall(T)
    G = [[0 for _ in range(len(T)+2)] for _ in range(len(T)+2)]

    n = len(T)
    s = n
    t = n+1

    for i in range(n):
        for j in range(n):
            if T[i][j] >= D and T[i][j] != inf and K[i] == 'B' and K[j] == 'G':
                G[i][j] = 1
                G[s][i] = 1
                G[j][t] = 1

    return edmonds_karp(G,s,t)

runtests( BlueAndGreen ) 
