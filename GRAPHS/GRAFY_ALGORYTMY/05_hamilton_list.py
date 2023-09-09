#ścieżki Hamiltona w DAGu

from collections import deque

def TopologicalSort(G):
    def DFSVisit(G, u):
        nonlocal visited
        nonlocal path

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)

        path.append(u)
    
    n = len(G)
    visited = [False for _ in range(n)]
    path = []

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    
    return path

def HamiltonPath(G):
    result = TopologicalSort(G)
    result.reverse()

    n = len(G)
    for ver in range(n-1):
        if result[ver+1] not in G[result[ver]]: return False
    
    return True