# Mamy graf skierowany i trzeba znaleźć cykl o minimalnej wadze
# Floyd warshall
# Sprawdzamy jaką wartość ma a->b + b->a i szukamy minimum

from math import inf

def floyd_warshall(G):
    n = len(G)
    D = [[inf for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                D[i][j] = G[i][j]
        D[i][i] = 0

    P = [[None for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                P[i][j] = i
        P[i][i] = None

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if( D[u][v] > D[u][k] + D[k][v] ):
                    P[u][v] = P[k][v]
                    D[u][v] = D[u][k] + D[k][v]

    for i in range(n):
        if(D[i][i] < 0): return False

    return D

def find_shortest_cycle(G):
    n = len(G)
    D = floyd_warshall(G)
    # dokonczyc