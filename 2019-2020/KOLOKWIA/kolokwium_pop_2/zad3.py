from zad3testy import runtests
from queue import PriorityQueue

def isConnected(m,n):
    A = [0]*10
    B = [0]*10

    while m != 0:
        A[m%10] += 1
        m //= 10

    while n != 0:
        B[n%10] += 1
        n //= 10

    for i in range(10):
        if A[i] and B[i]: return True

    return False

def createGraph(T):
    n = len(T)
    G = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            #print(T[u], T[v])
            if u != v and isConnected(T[u], T[v]):
                G[u].append([v, abs(T[u]-T[v])])

    return G

def dijkstra(G,s,t):
    n = len(G)
    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()

        if min_w < weights[u]:
            weights[u] = min_w

            if u == t: return min_w

            for v, weight in G[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v, u))

    return -1

def find_cost(P):
    #print(P)
    n = len(P)
    s = min(range(len(P)), key=P.__getitem__)
    t = max(range(len(P)), key=P.__getitem__)
    #print(s, t)
    G = createGraph(P)

    return dijkstra(G,s,t)

runtests(find_cost) 
