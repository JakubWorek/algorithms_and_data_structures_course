# Znajdujemy punkty artykulacji w wejściowym grafie
# Na ich podstawie numerujemy składowe grafu i punkty artykulacji
# Tylko usunięcie wierzchołka, który jest punktem artykulacji
# spowoduje, że graf przestanie być spójny.
# Następnie liczymy na ile komponentów rozpadnie się graf, jeżeli
# usuniemy dany punkt artykulacji.
# id to unkikatowy dla każdego punktu artykulacji numer, z pomocom
# którego wyznaczamy czy napotkaliśmy już daną składową, czy nie

from zad2testy import runtests

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
                

    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return is_art

def number_components(G, is_art):
    n = len(G)
    numbers = [-1] * n
    curr = 0

    def dfs(u):
        numbers[u] = curr
        for v in range(n):
            if G[u][v] and numbers[v] == -1 and not is_art[v]:
                dfs(v)

    for u in range(n):
        if numbers[u] == -1:
            if not is_art[u]: dfs(u)
            else: numbers[u] = curr
            curr += 1

    return numbers


def breaking(G):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    is_art = find_articulation_points(G)
    comp_num = number_components(G, is_art)
    found_comp = [-1]*n
    id = 0
    max_cnt = 0
    best_vertex = None

    for u in range(n):
        if is_art[u]:
            cnt = 0
            for v in range(n):
                if G[u][v] and found_comp[comp_num[v]] < id:
                    found_comp[comp_num[v]] = id
                    cnt +=1
            if cnt > max_cnt:
                max_cnt = cnt
                best_vertex = u
        id += 1

    return best_vertex

runtests( breaking )