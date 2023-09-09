# BFS - Breadth First Search - list
from queue import Queue


def BFS(graph, root):
    queue = Queue()
    visited = [False] * len(graph)
    result = []
    queue.put(root)
    visited[root] = True
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
    return result

def BFSl(G, s):
    Q = Queue()
    visited = [False]*len(G)
    dist = [float("inf")]*len(G)
        
    visited[s] = True
    dist[s] = 0
    Q.put(s)
    res = s

    while Q.empty() == False:
        u = Q.get()
        if dist[u] > dist[res]: res = u
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.put(v)
        
    return res, dist

# BFS - Breadth First Search - matrix

def BFSm(graph, root):
    queue = Queue()
    visited = [False] * len(graph)
    result = []
    queue.put(root)
    visited[root] = True
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for v in range(len(graph)):
            if visited[v] is False and graph[u][v] == 1:
                queue.put(v)
                visited[v] = True
    return result