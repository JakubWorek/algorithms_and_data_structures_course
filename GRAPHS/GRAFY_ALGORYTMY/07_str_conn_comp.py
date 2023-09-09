#silnie spójnych składowych

def SCC(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    new_graph = [[] for _ in range(len(graph))]
    transpose_graph(graph, new_graph)
    for j in range(len(visited)):
        visited[j] = False
    result = [[] for _ in range(len(graph))]
    index = 0
    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(new_graph, u, visited, result, index)
            index += 1
    return result


def dfs(graph, source, visited, result, index):
    visited[source] = True
    result[index].append(source)
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result, index)


def DFSUtil(graph, source, visited, stack):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFSUtil(graph, v, visited, stack)
    stack.append(source)


def transpose_graph(graph, new_graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)

################################

def create(G):

    n = len(G)
    modified_G = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            modified_G[v].append(u)

    return modified_G

def dfs_times(G):

    n = len(G)
    visited = [False] * n
    times = [0] * n
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)
        times[u] = time
        time += 1

    for u in range(n):                   # dla niekoniecznie niespojnego grafu
        if not visited[u]:
            dfs_visit(G, u)

    return times

def SSS(G):

    n = len(G)
    times = dfs_times(G)
    modified_G = create(G)
    visited = [False] * n
    colours = [0] * n             # ten sam kolor oznacza ze wierzcholki sa w tej samej SSS

    for i in range(n):
        times[i] = i, times[i]

    times.sort(key=lambda x: x[1], reverse=True)

    def dfs_visit(G, u, colour):
        visited[u] = True
        colours[u] = colour
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v, colour)

    colour = 0

    for i in range(n):
        if not visited[times[i][0]]:
            dfs_visit(modified_G, times[i][0], colour)
            colour += 1

    return colours


graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
print(SSS(graph))