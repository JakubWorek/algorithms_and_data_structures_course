from jumpertesty import runtests
from queue import PriorityQueue

def convert(graph):

    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                new_graph[u].append([v, graph[u][v]])
                new_graph[v].append([u, graph[u][v]])

    return new_graph

def jumper_dijkstra(G, s, t):
    n = len(G)
    G = convert(G)
    weights = [[float("inf")] * 3 for _ in range(n)]   
    # weights[u][0] - mozemy skorzystac z dwumilowych butow,
    # weights[u][1] - jeszcze nie mozemy
    # weights[u][2] - przed momentem skoczylismy
    parents = [[None] * 3 for _ in range(n)]           
    pq = PriorityQueue()

    pq.put((0, s, None, 1, 0))                            
    pq.put((0, s, None, 0, 0))                            
    pq.put((0, s, None, -1, 0))
    # 1 - mozemy wykorzystac dwumilowe buty 
    # 0 - nie mozemy                        
    # -1 - przed momentem skoczylismy

    def id(i):
        if i == -1: return 2
        if i == 0: return 1
        if i == 1: return 0
    # żeby wiedzieć, gdzie wpisać do tablicy weights

    while not pq.empty():
        min_w, u, parent, can_jump, prev_edge = pq.get()
        i = id(can_jump)

        if min_w < weights[u][i]:
            weights[u][i] = min_w
            parents[u] = parent

            if u == t: break

            # jeżeli możemy wykonać dwumilowy skok
            if can_jump == 1:
                for v, weight in G[u]:
                    # nie wykorzystujemy butow
                    if weights[v][0] == float("inf"):
                        pq.put((weights[u][1] + weight, v, u, 1, weight))                               
                    # wykorzystujemy buty
                    if weights[v][1] == float("inf"):
                        pq.put((weights[u][0] - prev_edge + max(prev_edge, weight), v, u, -1, weight))  
            # jeżeli jeszcze nie możemy skoczyć
            elif can_jump == 0:
                for v, weight in G[u]:
                    # nie wykorzystujemy butoww                                                                  
                    if weights[v][0] == float("inf"):
                        pq.put((weights[u][1] + weight, v, u, 1, weight))
            else:
                for v, weight in G[u]:
                    # czekamy
                    if weights[v][1] == float("inf"):                                                   
                        pq.put((weights[u][2] + weight, v, u, 0, weight))
    
    return min(weights[t])

def jumper_dp(G, s, t):
    n = len(G)
    D = [[float("inf")] * 2 for _ in range(n)]
    D[s][0] = D[s][1] = 0

    for parent in range(n):
        for u in range(n):
            for v in range(n):

                if G[parent][u] > 0 and G[u][v] > 0 and parent != u and parent != v and v != u: # skaczemy
                    if D[v][1] > D[parent][0] + max(G[parent][u], G[u][v]):
                        D[v][1] = D[parent][0] + max(G[parent][u], G[u][v])

                if G[u][v] > 0 and u != v:                                                      # idziemy normalnie
                    if D[v][0] > G[u][v] + min(D[u][0],D[u][1]):
                        D[v][0] = G[u][v] + min(D[u][0], D[u][1])

    return min(D[t])

runtests(jumper_dp)