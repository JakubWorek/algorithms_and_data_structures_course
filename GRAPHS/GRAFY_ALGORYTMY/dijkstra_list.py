# dijkstra

from queue import PriorityQueue

def dijkstra(graph, s):
    n = len(graph)
    q = PriorityQueue()
    dist = [float("inf") for _ in range(n)]
    parrent = [None for _ in range(n)]
    dist[s] = 0
    q.put((0,s))

    while not q.empty():
        distance, u = q.get()
        for v, time in graph[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                parrent[v] = u
                q.put((dist[v], v))
    
    return dist, parrent

def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def dijkstra_algorithm(graph, source):
    queue = PriorityQueue()
    queue.put((0, source))
    parent = [None] * len(graph)
    distance = [float("inf")] * len(graph)
    visited = [False] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    return parent, distance

G = [[(1, 5)], 
    [(0, 5), (2, 21), (3, 1)], 
    [(1, 21), (4, 7)], 
    [(1, 1), (4, 13), (5, 16)], 
    [(2, 7), (3, 13), (6, 4)], 
    [(3, 16), (6, 1)], 
    [(4, 4), (5, 1)]]
print(dijkstra(G,0))