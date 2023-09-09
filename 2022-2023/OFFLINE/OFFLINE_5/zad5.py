# Jakub Worek 24.04.2023 - 28.04.2023
#
# Opis algorytmu:
# Obrabiam wejściowe dane tworząc listę sąsiedztwa.
# Dodaję n-ty wierzchołek do grafu. Stanowi on połączenie między planetami osobliwymi.
# Łączę go z osobliwościami krawędziami o wadze 0.
# Obliczam długość najkrótszej ścieżki korzystając z algorytmu Dijkstry.
# 
# Złożoność:
# O(|E|*log|V|)

from zad5testy import runtests
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
    # tu prosze wpisac wlasna implementacje
    G = [[] for _ in range(n+1)]
    for u, v, time in E:
        G[u].append((v, time))
        G[v].append((u, time))
    for v in S:
        G[n].append((v, 0))
        G[v].append((n, 0))
    return dijkstra(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )