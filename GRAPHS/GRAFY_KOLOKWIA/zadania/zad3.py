def convert(T):
    n = len(T)
    G = [[] for _ in range(n)]
    for a in range(n):
        for b in range(a+1,n):
            if T[a][b] == 1:
                G[a] += [b]
            elif T[a][b] == 2:
                G[b] += [a]

    return G

def top_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = [None for _ in range(n)]
    indx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal indx
        indx -=1
        result[indx] = u

    for u in range(n):
        if not visited[u]: dfs(u)
    
    return result

def task(T):
    G = convert(T)
    print(G)
    return top_sort(G)

A = [[0, 0, 2, 1, 1],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [2, 0, 0, 0, 0]]

T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]

print(task(A))