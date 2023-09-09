# Jakub Worek 17.05.2023 - 21.05.2023
#
# Opis algorytmu:
# Dla każdego pracownika wykonujemy algorytm rekurencyjny w celu znalezienia
# optymalnego przypisania. 
# Dokonujemy przypisania pracownika u do maszyny v jeżeli ta jest wolna,
# lub pracownika m[v] który na niej pracował przeniesiemy na inną.
# Na końcu zwracamy ilość przypisań, która jest licznością maksymalnego
# skojarzenia w grafie dwudzielny (pracownicy - maszyny)
# 
# Złożoność:
# O(V*(V+E))

from zad6testy import runtests

def f(G, u, m, s):
    for v in G[u]:
        if s[v] == False:
            s[v] = True
            if m[v] == -1 or f(G, m[v], m, s):
                m[v] = u
                return True
    return False

def binworker( M ):
    # tu prosze wpisac wlasna implementacje
    n=len(M)
    m = [-1] * n
    r = 0
    for i in range(n):
        s = [False] * n
        if f(M, i, m, s): r += 1
    return r

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )