from zad3testy import runtests
from queue import PriorityQueue
from math import inf

def dijkstra(graph, s):
    n = len(graph)
    q = PriorityQueue()
    dist = [float("inf") for _ in range(n)]
    parrent = [None for _ in range(n)]
    dist[s] = 0
    q.put((0,s))

    while not q.empty():
        distance, u = q.get()
        for v, time in graph[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                parrent[v] = u
                q.put((dist[v], v))
    
    return dist


def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""
    n = len(G)
    dist1 = dijkstra(G,s)
    dist2 = dijkstra(G,t)

    if dist1[t] == inf or dist2[t] == inf: return 0

    visited = [False]*n
    cnt = [0]

    def dfs(G,u):
        visited[u] = True
        for v, w in G[u]:
            if dist1[u] + dist2[u] == dist1[v]+dist2[v] == dist1[t]\
                and dist1[u] + w == dist1[v]\
                and dist2[v] + w == dist2[u]: cnt[0] += 1
            if visited[v]: continue
            dfs(G,v)
    
    dfs(G,s)


    return cnt[0]

    
runtests( paths )


