def find_articulation_points(G):
    n = len(G)
    low    = [0] * n
    times  = [0] * n
    is_art = [False] * n
    time   = 0
    
    def dfs(root, u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        out_deg = 0
        
        for v in range(n):
            if not G[u][v] or v == parent: continue
            if not times[v]:
                out_deg += dfs(root, v, u) + u == root
                low[u] = min(low[u], low[v])
                if times[u] <= low[v]:
                    is_art[u] = True
            else:
                low[u] = min(low[u], times[v])
        
        return out_deg
                
    # Check all possible starting vertices as a graph doesn't have to be consistent
    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return is_art