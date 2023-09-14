# Dijkstra's algorithm for finding the shortest paths in weighted graph on adjacency matrix.
from queue import PriorityQueue
from math import inf


def relax(graph, u, v, distance, parent):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        parent[v] = u
        return True
    return False


def dijkstra_algorithm(graph, source):
    queue = PriorityQueue()
    queue.put((0, source))
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph[u])):
            if graph[u][v] != 0 and not visited[v]:
                if relax(graph, u, v, distance, parent):
                    queue.put((dist + graph[u][v], v))
        visited[u] = True
    return parent, distance