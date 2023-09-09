"""
W nowym grafie:

    Rozpatruje kazdy wierzcholek jako pare (u,v), ktora moze byc dowolna kombinacja wierzcholkow z pierwotnej
    macierzy

    Traktuje w takim grafie, ze istnieje krawedz miedzy (u,v) a (a,b) wtw, gdy istnieje krawedz (u,a) i (v,b)
    w grafie pierwotnym; dist(a,b) >= d; (u,v) != (b,a)

Uruchamiam bfsa na tym grafie, aby sprawdzic i znalezc odpowiednia sciezke, jesli takowa istnieje i da sie
dojechac do celu, zapisujac parentow w celu odzyskania rozwiazania (traktuje wagi krawedzi jako 1, bo nie wazne
jak szybko dojade, wazne czy dojade)

implementacyjnie wkladam do kolejki krotki (u,v), zeby nie musiec tworzyc calego nowego grafu

ALgorytmem floyda Warshalla obliczam doleglosci wszystkich:wszystkich aby sprawdzac to pozniej w czasie O(1)

Zlozonosc (V^4) - V^3 Floyd + V^4 BFS*|V'|, gdzie |V'| = |V|^2 
"""

from collections import deque
from zad1testy import runtests
from math import inf

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

    queue = deque()
    queue.append(s)
    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                parents[v] = u
                queue.append(v)

    return parents, visited

def keep_distance(G, A, B, d):
    n = len(G)
    m = n * n
    M = [[0 for _ in range(m)] for __ in range(m)]
    D = floyd_warshall(G)

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

    P, V= bfs(M,A*n + B)
    R = []
    i = B*n + A
    while i is not None:
        R.append((i//n, i%n))
        i = P[i]
    R.reverse()
    return R


runtests( keep_distance )