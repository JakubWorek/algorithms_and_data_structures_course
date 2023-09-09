from egzP1btesty import runtests 
from queue import PriorityQueue
from math import inf

def dijkstra(G, s, k):
    n = len(G)
    q = PriorityQueue()
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    parent = [None for _ in range(n)]
    q.put((0,s))

    while not q.empty():
        distance, u = q.get()
        if u == k: break

        for v, time in G[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                parent[v] = u
                q.put((dist[v], v))
    
    return parent, dist

def turysta( G, D, L ):
    #tutaj proszę wpisać własną implementację
    n = 0
    for i in range(len(G)):
        n = max(G[i][0],G[i][1], n)
        #print(n)
    n +=1

    GG = [[] for _ in range(n)]
    for u,v,time in G:
        GG[u].append((v,time))
        GG[v].append((u,time))

    #print(GG)
    P, DI = dijkstra(GG, D, L)
    #print(DI)

    PTH = []
    ver = L
    while P[ ver ] != None:
        PTH.append((P[ver], ver, ))
        ver = P[ver]
    
    if len(PTH) == 4:
        return DI[L]
    else:
        best_dist = float("inf")
        for edg in PTH:
            for kr in G:
                if (edg[0] == kr[0] and edg[1] == kr[1]) or\
                    (edg[1] == kr[0] and edg[0] == kr[1]):
                    time = kr[2]
                    break
            GG[edg[0]].remove((edg[1], time))
            GG[edg[1]].remove((edg[0], time))

            par, dis = dijkstra(GG,D,L)
            path = 0
            vert = L
            while par[vert] != None:
                path+=1
                vert = par[vert]
            if path == 4:
                if dis[L] < best_dist:
                    best_dist = dis[L]
            
            GG[edg[0]].append((edg[1], time))
            GG[edg[1]].append((edg[0], time))
    
    return best_dist

#################################################

def prepare_graph(G):
    n = G[0][0]

    for e in G:
        n = max(n, e[0], e[1])
    n += 1
    
    G_ = [[-1 for _ in range(n)] for _ in range(n)]
    G2_ = [[] for _ in range(n)]
    for (u, v, d) in G:
        if u != v:
            G_[u][v] = d
            G_[v][u] = d
            G2_[v].append((u,d))
            G2_[u].append((v,d))
    
    return G_, G2_, n

def turysta1(G, D, L):
    G_, G2_, n = prepare_graph(G)
    minl = float("inf")
    for vD,w1 in G2_[D]:
        if vD == L: continue
        for vL,w2 in G2_[L]:
            if vL == D: continue
            for i in range(n):
                if i == vD or i == vL: continue
                if G_[vD][i] > 0 and G_[i][vL] > 0:
                    w = w1 + w2 + (G_[vD][i] + G_[i][vL])
                    if w < minl: minl = w

    return minl

###################################################3

def rek(G, u, v, k, n):
    if k == 0 and u == v: return 0
    if k == 1 and G[u][v] != float("inf"): return G[u][v]
    if k <= 0: return float("inf")

    res = float("inf")
    for i in range(n):
        if G[u][i] != float("inf") and u != i and v != i:
            rec_res = rek(G,i,v,k-1,n)
            if rec_res != float("inf"):
                res = min(res, G[u][i] + rec_res)
    
    return res

def turysta2(G, D, L):
    n = 0
    for i in range(len(G)):
        n = max(G[i][0],G[i][1], n)
        #print(n)
    n +=1
    GG = [[float("inf") for _ in range(n)] for _ in range(n)]
    for u, v, time in G:
        GG[u][v] = time
        GG[v][u] = time

    return rek(GG, D, L, 4, n)

################################################

def turysta3(G, D, L):
    size = 0
    for v, u, w in G:
        size = max(size, u)
    N = [[]for _ in range(size + 1)]
    for v, u, w in G:
        N[v].append((u, w))
        N[u].append((v, w))
    distance = [[inf]*3 for _ in range(size + 1)]
    q = PriorityQueue()
    for i in range(3):
        distance[D][i] = 0
    q.put((0, D, 3))
    while not q.empty():
        w1, v, ilosc = q.get()
        for u, w2 in N[v]:
            if ilosc > 0 and u != L:
                if distance[u][ilosc - 1] > w1 + w2:
                    distance[u][ilosc - 1] = w1 + w2
                    q.put((distance[u][ilosc - 1], u, ilosc - 1))
            elif ilosc == 0 and u == L:
                distance[L][0] = min(distance[L][0], w1 + w2)
    return min(distance[L])

################################################
G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7),
(4, 5, 6), (3, 6, 8),
(4, 6, 1), (5, 6, 1)
]
D = 0
L = 6

#print(turysta2(G,D,L))
runtests ( turysta3 )