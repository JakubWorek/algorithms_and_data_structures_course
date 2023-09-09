from zad2testy import runtests
from queue import PriorityQueue
from math import inf

def let( ch ): return ord(ch) - ord("a")

def create(L, E):
    n = len(L)
    G = [['', []] for _ in range(n)]

    for i in range(n):
        G[i][0] = L[i]

    for edge in E:
        G[edge[0]][1].append((edge[1], edge[2]))
        G[edge[1]][1].append((edge[0], edge[2]))

    return G


def addBegin(G, W):
    n = len(G)
    G.append(['', []])

    for i in range(n):
        if G[i][0] == W[0]:
            G[n][1].append((i, 0))

    return n


def minCost(G,W,s):
    n = len(G)
    m = len(W)

    DP = [[inf]*m for _ in range(n)]

    def dfs(u, i):
        if i == m: return 0
        if DP[u][i] == inf:
            for v, w in G[u][1]:
                if G[v][0] == W[i]:
                    DP[u][i] = min(DP[u][i], dfs(v, i+1)+w)
        return DP[u][i]
    
    sol = dfs(s, 0)
    return sol


def letters( G, W ):
    # tu prosze wpisac swoje rozwiazanie
    L, E = G
    G = create(L, E)
    beg = addBegin(G, W)
    print(*G, sep='\n')
    return minCost(G,W,beg)

runtests( letters )