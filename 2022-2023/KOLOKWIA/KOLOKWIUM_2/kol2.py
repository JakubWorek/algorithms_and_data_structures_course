# Jakub Worek
#
# Robię krawędzie z grafu, sortuję je po wagach, 
# biorę pierwsze n-1 krawędzi i sprawdzam dfs-em czy tworzą drzewo.
#
# Złożoność: O(EV)

from kol2testy import runtests

def convertToEdges(graph):
    n = len(graph)
    edges = []
    for vert in range(n):
        for edge in graph[vert]:
            if vert < edge[0]:
                edges.append((vert, edge[0], edge[1]))
    
    return edges

def checkTree(edges, n):
    G = [[] for _ in range(n)]
    for edge in edges:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    
    visited = [False] * n

    def dfs_visit(u, graph, visited):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v, graph, visited)

    dfs_visit(0, G, visited)
    for i in range(n):
        if not visited[i]: return False
    return True

def sumTree(edges):
    sum = 0
    for edge in edges:
        sum += edge[2]
    return sum


def beautree(G):
    n = len(G)
    E = convertToEdges(G) 
    E.sort(key=lambda x: x[2]) 

    for i in range(len(E)-n+1):
        if(checkTree(E[i:i+n-1], n)):
            return sumTree(E[i:i+n-1])
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
