from zad9testy import runtests
from math import inf
from collections import deque


def bfs(graph, s, t, parent):
    queue = deque()
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while queue:
        u = queue.popleft()
        if u == t: return True
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                parent[v] = u
                if v == t: return True
                visited[v] = True
                queue.append(v)
    return visited[t]


def edmonds_karp_algorithm(G, s, t):
    if s == t: return 0
    n = len(G)
    graph = [row[:] for row in G]
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
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


def maxflow( G,s ):
    # tu prosze wpisac wlasna implementacje
    maxi = 0
    for i, j, k in G: maxi = max(max(maxi, i), j )
    n = maxi+2
    newG = [[0]*n for _ in range(n)]
    for skad, dokad, ile in G:
        newG[skad][dokad] = ile

    n-=1
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if i != s and j != s and i != j:
                newG[i][n], newG[j][n] = inf, inf
                currflow = edmonds_karp_algorithm(newG, s, n)
                res = max(res, currflow)
                newG[i][n] = newG[j][n] = 0
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )