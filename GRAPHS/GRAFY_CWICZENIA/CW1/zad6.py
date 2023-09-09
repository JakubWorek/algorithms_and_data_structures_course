# Proszę zaimplementować algorytm BFS tak, żeby znajdował najkrótsze ścieżki w grafie i następnie,
# żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego do wskazanego wierzchołka.
# reprezentacja: lista

from queue import Queue
from math import inf

def shortest_path(G,start,end):

    n=len(G)
    visited=[False for _ in range(n)]
    parent = [-1] * n

    q=Queue()
    q.put(start)
    visited[start] = True

    while not q.empty():
        u=q.get()

        if u == end:
            break

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v]=u
                q.put(v)


def find_shortest_paths(graph):
    queue = Queue()
    source = 0
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    distance = [inf] * len(graph)
    distance[source] = 0
    while not queue.empty():
        u = queue.get()
        min_distance = inf
        for v in graph[u]:
            if not visited[v]:
                for g in graph[v]:
                    min_distance = min(min_distance, distance[g])
                distance[v] = min_distance + 1
                queue.put(v)
                visited[v] = True
    return distance