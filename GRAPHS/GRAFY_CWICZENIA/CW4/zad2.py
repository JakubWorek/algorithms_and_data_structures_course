# Proszę zaproponować algorytm obliczający domknięcie przechodnie 
# grafu reprezentowanego w postaci
# macierzowej (domknięcie przechodnie grafu G to taki graf H, 
# że w H mamy krawędź z u do v wtedy
# i tylko wtedy gdy w G jest ścieżka skierowana z u do v).

def closure(G):
    n = len(G)
    R = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                R[i][j] = 1

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if G[u][v] == 1 or (G[u][k] == 1 and G[k][v] == 1):
                    R[u][v] = 1
    
    return R


graph = [[0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0]]

R = closure(graph)
for i in range(len(graph)):
    print(R[i])
