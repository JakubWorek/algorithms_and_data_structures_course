# DFS - Depth First Search - list

# 1st solution

def DFS(graph, root):
    visited = [False] * len(graph)
    result = [root]

    def dfs_visit(u, graph, visited, result):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                result.append(v)
                dfs_visit(v, graph, visited, result)

    dfs_visit(root, graph, visited, result)
    return result


# 2nd solution

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited

# DFS - Depth First Search - matrix

def DFSm(graph, root):
    visited = [False] * len(graph)
    result = []
    dfs_visitm(root, graph, visited, result)
    return result


def dfs_visitm(u, graph, visited, result):
    visited[u] = True
    result.append(u)
    for i in range(len(graph)):
        if visited[i] is False and graph[u][i] == 1:
            dfs_visitm(i, graph, visited, result)