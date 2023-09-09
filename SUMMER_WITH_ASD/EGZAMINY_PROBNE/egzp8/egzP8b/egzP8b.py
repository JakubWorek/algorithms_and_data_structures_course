# Algorytmem Floyda-Warshalla wyznaczamy długości najkrótszych ścieżek
# Następnie przechodzimy i sumujemy długość trasy robota

from egzP8btesty import runtests
from math import inf

def floyd_warshall(graph):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance

def robot( G, P ):
    n = len(G)
    GG = [[0 for _ in range(n)] for __ in range(n)]
    for u in range(n):
        for v in G[u]:
            GG[u][v[0]] = v[1]
            GG[v[0]][u] = v[1]

    dist = floyd_warshall(GG)
    sol = 0
    curr = P[0]
    for i in range(1, len(P)):
        sol += dist[curr][P[i]]
        curr = P[i]

    return sol
    
runtests(robot, all_tests = True)
