# Opis algorytmu:
# Znajduję najkrótszą scieżkę pomiędzy wskazanymi wierzchołkami korzystając z bfs
# Odtwarzam jej krawędzie na podstawie tablicy parents
# Ścieżka ma możliwość wydłużenia się tylko jeżeli będziemy usuwali krawędzie
#   wyznaczonej wcześniej najkrótszej ściezki
# Idąc po kolejnych krawędziach ścieżki i je chwilowo usuwając wyznaczam długość
#   nowej najkrótszej ścieżki korzystając z algorytmu bfs
#
# Złożoność algorytmu:
# O(V*(V+E))

from zad2testy import runtests
from collections import deque


def bfs(G, s):
    # klasyczny bfs
    visited = [False] * len(G)
    visited[s] = True
    distances = [float("inf")] * len(G)
    distances[s] = 0
    parents = [-1] * len(G)

    queue = deque()
    queue.append(s)
    while len(queue) > 0:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)

    return visited, distances, parents


def enlarge( G, s, t ):
    # wyznaczamy odległości od początkowego wierzchołka
    odwiedzone, odleglosci, rodzic = bfs(G, s)

    odleglosc1 = odleglosci[t]
    # sprawdzam czy ścieżka istnieje
    if odleglosc1 == float("inf"): return None

    # wyznaczamy najkrótszą ścieżkę od końcowego do 
    # początkowego wierzchołka
    sciezka = []
    wierzcholek = t
    while rodzic[ wierzcholek ] != -1:
        sciezka.append((rodzic[wierzcholek], wierzcholek))
        wierzcholek = rodzic[wierzcholek]

    del odwiedzone, odleglosci, rodzic

    for krawedz in sciezka:
        # chwilowo usuwamy krawędź z nakrótszej ścieżki
        G[krawedz[0]].remove(krawedz[1])
        G[krawedz[1]].remove(krawedz[0])

        # liczymy dystanse od nowa
        odwiedzone, odleglosci, rodzic  = bfs(G, s)

        odleglosc2 = odleglosci[t]
        if odleglosc2 > odleglosc1: return krawedz

        # dodajemy usuniętą krawędź ścieżki do grafu
        G[krawedz[0]].append(krawedz[1])
        G[krawedz[1]].append(krawedz[0])
        
        del odwiedzone, odleglosci, rodzic

    return None

runtests( enlarge ) 
