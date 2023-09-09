from egzP5btesty import runtests 

def DFS(G, V, i, B):
    V[i] = 1
    for v in G[i]:
        if V[v] == 0 and v != B:
            DFS(G,V,v,B)

def articulation_n2(G):
    n = len(G)
    points = 0
    for i in range(n):
        V = [0 for _ in range(n)]
        if i != 0:
            DFS(G, V, 0, i)
        else: DFS(G, V, 1, 0)

        if sum(V) < n-1: points += 1
    
    return points

def koleje ( B ):
    #preprocessing tablicy B do znajdywania punktów artykulacji
    n = len(B)
    for i in range(n):
        B[i] = (min(B[i][0], B[i][1]), max(B[i][0], B[i][1]))
    B.sort(key = lambda x: (x[0], x[1]))

    # tworzenie grafu
    m = 0
    for el in B:
        m = max(m, el[1])
    m+=1

    G = [[] for _ in range(m)]
    last = None
    for i in range(n):
        if last != B[i]:
            last = B[i]
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])

    # znajdywanie punktów artykulacji
    return articulation_n2(G)

runtests ( koleje, all_tests=False )