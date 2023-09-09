from zad2testy import runtests

def rec(L,K,T,sol,idx):
    if len(sol) == len(L): return True

    for j in range(len(L)):
        if (sol[idx] % (10**K)) == (T[j][0] // (10**K)) and T[j][1] == False:
            sol.append(T[j][0])
            T[j][1] = True
            rec(L,K,T,sol,idx+1)

    if len(sol) != len(L):
        idx -=1
        val = sol.pop()
        T[L.index(val)][1] = False
    

def order(L,K):
    start = min(L)
    T = [0,False]*len(L)
    for i in range(len(L)):
        if L[i] == start: T[i] = [L[i], True]
        else: T[i] = [L[i], False]

    sol = [start]
    rec(L,K,T,sol,0)
    return sol

###################################3

def check(a, b, k):
    m = 10 ** k
    return a % m == b // m


def create_graph(L, k):
    n = len(L)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if check(L[i], L[j], k):
                graph[i].append(j)
            if check(L[j], L[i], k):
                graph[j].append(i)

    return graph


def dfs(L, g, v, sorted_g, visited):
    visited[v] = True
    for e in g[v]:
        if visited[e] is False:
            dfs(L, g, e, sorted_g, visited)

    sorted_g.insert(0, L[v])


def topological_sort(L, g, k):
    n = len(g)
    visited = [False] * n
    path = []
    for e in range(n):
        if visited[e] is False:
            dfs(L, g, e, path, visited)

    for i in range(1, n):
        if not check(path[i - 1], path[i], k):
            return None

    return path


def order_graph(L, k):
    return topological_sort(L, create_graph(L, k), k)


runtests( order )