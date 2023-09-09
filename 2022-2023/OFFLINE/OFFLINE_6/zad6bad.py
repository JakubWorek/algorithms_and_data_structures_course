# Jakub Worek
#
# Działa, ale wolno.


from zad6testy import runtests
from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]

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


def edmonds_karp_algorithm(graph, s, t):
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


def binworker( M ):
    # tu prosze wpisac wlasna implementacje
    m=len(M)
    n = 2*m + 2
    G = [[0 for _ in range(n)] for __ in range(n)]

    for worker in range(m):
        for mashine in M[worker]:
            G[worker][m+mashine] = 1
    start = n-2
    end = n-1
    for i in range(m):
        G[start][i] = 1
    for i in range(m, 2*m):
        G[i][end] = 1

    return edmonds_karp_algorithm(G, start, end)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
