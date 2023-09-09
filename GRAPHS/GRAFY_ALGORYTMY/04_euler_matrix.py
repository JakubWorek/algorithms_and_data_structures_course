#cyklu Eulera w grafie

def euler_cycle(G):
    def DFSVisit(G, u):
        nonlocal result
        n = len(G)

        for i in range(n):
            if G[u][i] == 1:
                G[u][i] = G[i][u] = 0
                DFSVisit(G, i)
        
        result.append(u)

    n = len(G)
    for i in range(n):
        edges = 0
        for j in range(n):
            if(G[i][j] == 1): edges += 1
        
        if edges%2 == 1: return None
    
    result = []
    DFSVisit(G, 0)
    result.reverse()
    return result

G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

print(euler_cycle(G))