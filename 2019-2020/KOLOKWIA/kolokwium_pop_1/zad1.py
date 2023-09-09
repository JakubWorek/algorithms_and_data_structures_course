from zad1testy import runtests
from queue import PriorityQueue

def dijkstra(G, F, d, s, t):
    n = len(G)
    D = [float('inf')] * n
    D[s] = 0
    fuelLeft = [0] * n
    fuelLeft[s] = d
    Parent = [-1] * n
    Q = PriorityQueue()
    Q.put((D[s], s))

    while not Q.empty():
        _, u = Q.get()
        for v in range(n):
            if G[u][v] != -1  and G[u][v] <= fuelLeft[u]:
                if D[v] >= D[u] + G[u][v]:
                    D[v] = D[u] + G[u][v]
                    if v in F:
                        fuelLeft[v] = d
                    else:
                        fuelLeft[v] = fuelLeft[u] - G[u][v]
                    Q.put((D[v], v))
                    Parent[v] = u
    return Parent


def jak_dojade(G, P, d, s, t):
    # tu prosze wpisac wlasna implementacje
    parents = dijkstra(G, P, d, s, t)
    path = []
    curr = t
    while curr != s:
        if curr == -1:
            return None
        path.append(curr)
        curr = parents[curr]
    path.append(s)
    return path[::-1]

runtests( jak_dojade ) 
