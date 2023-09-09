from zad7testy import runtests

def ispath(G, u, path, n, visited, gate, find):
        if len(path) == n and 0 in G[u][gate]:
            return True

        for v in G[u][gate]:
            if not visited[v] and not find:
                if u not in G[v][0]:
                    visited[v] = True
                    path.append(v)
                    find = ispath(G, v, path, n, visited, 0, find)
                    if find:
                        return find
                    visited[v] = False
                    path.pop()
                elif u not in G[v][1]:
                    visited[v] = True
                    path.append(v)
                    find = ispath(G, v, path, n, visited, 1, find)
                    if find:
                        return find
                    visited[v] = False
                    path.pop()
        
        return False

def droga( G ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    find = False
    visited = [False] * n
    path = [0]
    visited[0] = True
    res = ispath(G, 0, path, n, visited, 0, find)

    if res: return path
    else: return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )