from kol3btesty import runtests
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

def airports( G, A, s, t ):
    G.append([])
    n = len( G )
    for i in range(n-1):
        G[n-1].append( (i, A[i]) )
        G[i].append( (n-1, A[i]) )
    return dijkstra(G, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = False )