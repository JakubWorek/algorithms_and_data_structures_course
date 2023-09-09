# Ile jest wspolnych składowych oparte o DFS

def ileSkladowych(G):

    def DFSvisit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                DFSvisit(G,v)

    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]

    licznik = 0

    for u in range(n):
        if not visited[u]:
            licznik += 1
            DFSvisit(G,u)

    return licznik