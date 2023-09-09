from kol3atesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, k):
    n = len(G)
    q = PriorityQueue()
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    q.put((0,s))

    while not q.empty():
        distance, u = q.get()
        if u == k: break

        for v, time in G[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                q.put((dist[v], v))
    
    return dist[k] if dist[k] != float("inf") else None

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n+1)]
    for u, v, time in E:
        G[u].append((v, time))
        G[v].append((u, time))
    for v in S:
        G[n].append((v, 0))
        G[v].append((n, 0))
    return dijkstra(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = False )