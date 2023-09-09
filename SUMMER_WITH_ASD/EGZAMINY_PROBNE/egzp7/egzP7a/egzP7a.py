# Tworzymy macierz sąsiedztwa z dodatkowymi wierzchołkami 
# Na super wpływ i ujście z grafu
# Następnie wyznaczamy maksymalny przepływ i obliczamy wynik końcowy
#
# Złożoność: 
# Przygotowanie grafu: O(n^2)
# Metoda forda fulkersona: O(V*E*Fmax)
#   Fmax jest rzędu n, E jest rzędu n, V wynosi n
# Ostatecznie: O(n^3)

from egzP7atesty import runtests 
from math import inf

def dfs_visit(graph, source, visited, parent):
    visited[source] = True
    for v in range(len(graph)):
        if not visited[v] and graph[source][v] != 0:
            parent[v] = source
            dfs_visit(graph, v, visited, parent)


def dfs(graph, s, t, parent):
    visited = [False] * len(graph)
    dfs_visit(graph, s, visited, parent)
    return visited[t]


def ford_fulkerson(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while dfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow

def akademik( T ):
    s = len(T)*2
    t = s+1
    n = t+1
    n1 = len(T)

    G=[[0 for __ in range(n)] for _ in range(n)]

    for i in range(n1):
        for j in range(3):
            if T[i][j] != None:
                G[i][n1+T[i][j]] = 1

    for i in range(n1):
        G[s][i] = 1
        G[n1+i][t] = 1

    pustych = 0
    for i in range(n1):
        if T[i] == (None, None, None): pustych += 1

    return n1 - pustych - ford_fulkerson(G, s, t)

runtests ( akademik )