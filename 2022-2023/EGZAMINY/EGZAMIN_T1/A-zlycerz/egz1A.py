# Jakub Worek 13.07.2023
#
# Wyliczam podstawowy koszt przejścia po grafie dijkstrą
# Następnie przechodząc po kolejnych wierzchołkach wybieram który obrabuję
# Wyliczam koszt dojścia do obrabowywowanego wierzchołka,
# nakładam na graf większe ceny, wyliczam koszt dojścia do mety od
# obrabowanego zamku i nakładam stare podstawowe ceny na graf.
# 
# Złożoność:
# V razy wykonuję podwójnie algorytm Dijkstry zatem
# szacuję na O(V*ElogV), ale w pesymistycznym przypadku 
# E = V^2
# Zatem ostatecznie: O(V^3logV)

from egz1Atesty import runtests
from queue import PriorityQueue

def dijkstra(graph, s, t):
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
    return dist[t]

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n = len(G)
  koszt_bez_rabowania = dijkstra(G, s, t)
  min_koszt = koszt_bez_rabowania
  for v in range(n):
      if v == s: koszt_przed_obrabowaniem = 0
      else: koszt_przed_obrabowaniem = dijkstra(G, s, v)
      for wierzcholek in range(n):
          for kr in range(len(G[wierzcholek])):
            nowa_tupla = (G[wierzcholek][kr][0], (2*G[wierzcholek][kr][1]) + r)
            G[wierzcholek][kr] = nowa_tupla
      ile_zrabowal = V[v]
      if v == t: koszt_po_obrabowaniu = 0
      else: koszt_po_obrabowaniu = dijkstra(G, v, t)
      koszt_przejscia = koszt_przed_obrabowaniem + koszt_po_obrabowaniu - ile_zrabowal
      min_koszt = min(min_koszt, koszt_przejscia)
      for wierzcholek in range(n):
          for kr in range(len(G[wierzcholek])):
            nowa_tupla = (G[wierzcholek][kr][0], (G[wierzcholek][kr][1]-r)//2)
            G[wierzcholek][kr] = nowa_tupla
  return min_koszt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
