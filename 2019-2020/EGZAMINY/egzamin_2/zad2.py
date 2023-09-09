# W Algorytmie korzystam z algorytmu Kruskala.
# Na początku tworzę graf pełny w postaci listy krawędzi o krawędziach ważonych
# o wagach wyliczonych z podanego w zadaniu wzoru. Krawędzie sortuje rosnąco według wag.
# Następnie w pętli wyznaczam minimalne drzewo rozpinające stworzonego grafu, sprawdzam
# i aktualizuje minimum ( minimalną liczbę dni będącą wynikiem ) oraz usuwam najmniejszą krawędź.
# Robię to dopóki graf jest spójny. Kiedy graf przestaje być spójny zwracam wynik

from zad2testy import runtests
from math import ceil

def KRUSKAL(G,V, best):
    parent = [i for i in range(V)]
    rank = [0] * V

    # struktura find-union z wykładu, przerobiona na tablice zamiast klas
    def find(x):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a = find(x)
        b = find(y)
        if a == b: return
        if rank[a] > rank[b]: parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]: rank[b] += 1

    MST = []
    for a, b, c in G:
        if find(a) != find(b):
            MST.append((a, b, c))
            if abs(c - MST[0][2]) >= best: return MST[0], False # jeśli otrzymaliśmy liczbę dni większą niż dotychczasowy najlepszy wynik lub równą, to nie ma sensu sprawdzać dalej
            elif len(MST) == V - 1: break # jedną z własności drzew jest, że V = E + 1, więc jeśli utworzone MST ma już tyle krawędzi to nie ma potrzeby iterować dalej po krawędziach
            union(a, b)

    return MST, True

def highway( A ):
    # tu prosze wpisac wlasna implementacje
    G = []
    V = len(A)
    mini = float("inf")

    #tworzymy listę krawędzi
    for i in range(V-1):
        for j in range(i+1, V):
            G.append((i, j, ceil(((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2)**0.5)))

    G = sorted(G, key=lambda weight: weight[2])
    while len(G) >= V-1:
        B, flag = KRUSKAL(G,V,mini)
        if not flag:
            G.remove(B)
            continue
        if len(B) < V - 1: break
        mini = min(mini, abs(B[0][2] - B[-1][2]))
        G.remove(B[0])
    return None if mini == float("inf") else mini
        

runtests( highway ) 
