# Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
# alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
# W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
# funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
# układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
# Jeśli takiej ścieżki nie ma, należy zwrócić -1.

# Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para
# (L, E). L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku i. E jest listą krawędzi
# i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki
# połączone krawędzią o wadze w.

# Przyklad.

# W reprezentacji przyjętej w zadaniu mógłby być zapisany jako:

# L = ["k","k","o","o","t","t"]
# E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
# G = (L,E)

# Rozwiązaniem dla tego grafu i słowa W = "kto" jest 4 i jest osiągane przez ścieżkę 1 − 4 − 3. Inna
# ścieżka realizująca to słowo to 1 − 4 − 2, ale ma koszt 8


from zad2testy import runtests
from queue import PriorityQueue
from math import inf

def create(E):
    n = 0
    for u, v, _ in E:
        n = max(n, max(u, v))
    n+=1

    G = [[] for _ in range(n)]

    for u, v, w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    
    return G


def get_indexes(char, L):
    indexes = []
    for i, letter in enumerate(L):
        if letter == char:
            indexes.append(i)
    return indexes


def dijkstra(G, L, s, W):
    n = len(G)
    p = len(W)
    Q = PriorityQueue()
    Q.put((0, s, 0))

    while not Q.empty():
        dist, u, ind = Q.get()
        if ind + 1 == p: return dist

        for v, time in G[u]:
            if L[v] == W[ind + 1]:
                Q.put((dist+time, v, ind+1))

    return inf


def letters(G, W):
    L, E = G
    graph = create(E)
    arr_indexes = get_indexes(W[0], L)

    min_w = float("inf")
    for idx in arr_indexes:
        min_w = min(min_w, dijkstra(graph, L, idx, W))
        
    return min_w if min_w != float("inf") else -1

runtests(letters)