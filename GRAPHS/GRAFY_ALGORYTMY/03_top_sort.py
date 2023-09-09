# Top sort
# DAG is a directed acyclic graph
# Topological sorting of DAG consists in arranging the vertices in order that the edges point
# only from left to right.


def dfs(graph, source, visited, result):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result)
    result.insert(0, source)


def topological_sort(graph):
    visited = [False] * len(graph)
    result = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, result)
    return result