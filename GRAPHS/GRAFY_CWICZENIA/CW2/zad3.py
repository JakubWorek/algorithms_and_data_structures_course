# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
# miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci
# (x, y, c), gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na grupki tak, żeby
# każda grupka mogła przebyć trasę bez rozdzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
# dostali się z A do B.

from queue import PriorityQueue
from math import inf, ceil

def tourGuide(G, A, B, K):
    def comparator(u,v):
        nonlocal newG
        nonlocal distance
        nonlocal parent

        actual_distance = min(distance[u], newG[u][v])
        if actual_distance > distance[v]:
            distance[v] = actual_distance
            parent[v] = u
            return True
        
        return False

    n = len(G)

    #robimy macierz sąsiedztwa z wagami
    max_vertex = 0
    max_weight = 0

    for i in range(n):
        max_vertex = max(max_vertex, G[i][0], G[i][1])
        max_weight = max(max_weight, G[i][2])
    
    newG = [[0]*(max_vertex +1) for _ in range(max_vertex+1)]
    for i in range(n):
        newG[G[i][0]][G[i][1]] = newG[G[i][1]][G[i][0]] = G[i][2]
    max_weight+=1

    # BFS na macierzy 
    lennG = len(newG)
    queue = PriorityQueue()
    queue.put((max_weight, A))
    visited = [False for _ in range(lennG)]
    visited[A] = True
    distance = [-1] * lennG
    distance[A] = inf
    parent = [None] * lennG

    while not queue.empty():
        distans, u = queue.get()
        for v in range(lennG):
            if not visited[v] and newG[u][v] != 0:
                if comparator(u,v):
                    queue.put((max_weight - distance[v], v))
        visited[u] = True

    # odtwarzamy trasę
    min_weight = inf
    tour = []

    while B is not None:
        tour.append(B)
        min_weight = min(min_weight, distance[B])
        B = parent[B]
    
    n_o_groups = ceil(K / min_weight)
    tour.reverse()

    return n_o_groups, tour


graph = [(0, 1, 12), (0, 2, 10), (1, 3, 11), (1, 4, 7), (2, 4, 8), (2, 6, 14),
        (3, 5, 8), (4, 6, 8), (5, 7, 11), (6, 7, 6)]
city_a = 0
city_b = 7
print(tourGuide(graph, city_a, city_b, 20))