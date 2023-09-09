# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można
# osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf
# zawiera dobry początek.

def haveGoodStart(G):
    def DFSVisit(G, u):
        nonlocal visited
        nonlocal time
        nonlocal process_time

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)
        
        time +=1
        process_time[u] = time


    n = len(G)
    visited = [False for _ in range(n)]
    time = 0
    process_time = [-1 for _ in range(n)]

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)

    for i in range(n):
        if process_time[i] == n:
            index = i
            visited = [False for _ in range(n)]
            time = 0
            DFSVisit(G, index)
            return time == n
    
    return False


graph = [[1],
         [2],
         [0, 3],
         [4],
         []]

print(haveGoodStart(graph))