from kolutesty import runtests
from collections import deque

def getdegree(depends):
    n = len(depends)
    degarr = [0] * n
    for i, arr in enumerate(depends):
        for j in arr:
            degarr[j] += 1
    return degarr

def bfs(depends, degree, disk):
    n = len(depends)
    dist = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    Q = deque()

    # dodajemy do kolejki wierzchołki bez zależności od innych
    for i in range(n):
        if not degree[i]:
            Q.append(i)
            dist[i] = 0
            visited[i] = True
    
    while Q:
        u = Q.popleft()

        if parents[u] is not None:
            if disk[parents[u]] != disk[u]:
                dist[u] = dist[parents[u]] + 1
            else: dist[u] = dist[parents[u]]
        
        for v in depends[u]:
            degree[v] -=1
            if not visited[v] and degree[v] <=0:
                visited[v] = True
                parents[v] = u
                if disk[v] == disk[u]: Q.appendleft(v)
                else: Q.append(v)
    
    return max(dist)

def swaps( disk, depends ):
    degree = getdegree(depends)
    return bfs(depends, degree, disk)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = False )

