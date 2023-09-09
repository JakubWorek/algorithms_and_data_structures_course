#Sprawdzanie dwudzielnosci grafu oparte o bfs

from queue import Queue

# zmodyfikowany bfs
def isDwudzielny(G,s):
    q=Queue()
    n=len(G)
    colors=[-1 for _ in range(n)]
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]

    q.put(s)
    colors[s]=1
    while not q.empty():
        u=q.get()
        for v in range(n):
            if v != u and G[u][v] == True and not visited[v]:
                visited[v]=True
                parent[v]=u
                '''
                parrent_col=colors[u]
                if parrent_col == 1:
                    col=2
                elif parrent_col == 2:
                    col = 1
                '''
                colors[v]=3-colors[u]
                q.put(v)
            elif v != u and G[u][v] == True and visited[v]\
                and colors[v] == colors[u]: return False
    
    return True