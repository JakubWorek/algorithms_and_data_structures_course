# Jakub Worek 13.07.2023
#
# Wyliczam koszty przejscia przed i po rabowaniu
# Następnie przechodząc po kolejnych wierzchołkach wybieram który obrabuję
# Obliczam koszt całkowitego przejscia i zwracam minimum
# 
# Złożoność: O(V^2logV)

from egz1Atesty import runtests
from queue import PriorityQueue

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

def gold(G,V,s,t,r):
    n = len(G)
    koszty_przed = dijkstra(G, s)

    # zmieniamy graf
    for wierzcholek in range(n):
            for kr in range(len(G[wierzcholek])):
                nowa_tupla = (G[wierzcholek][kr][0], (2*G[wierzcholek][kr][1]) + r)
                G[wierzcholek][kr] = nowa_tupla

    koszty_po = dijkstra(G, t)
    min_koszt = koszty_przed[t]

    for v in range(n):
        ile_zrabowal = V[v]
        koszt_przejscia = koszty_przed[v] + koszty_po[v] - ile_zrabowal
        min_koszt = min(min_koszt, koszt_przejscia)
    
    return min_koszt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
