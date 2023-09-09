from zad4testy import runtests

def f(DP,buildings, students, parent, cost, i, p):
    if i is None: return buildings
    if i == 0:
        if p>cost[0]:
            buildings.append(0)
        return buildings
    if DP[i-1][p] == DP[i][p]:
        return f(DP, buildings, students, parent, cost, i-1, p)
    buildings.append(i)
    return f(DP, buildings, students, parent, cost, parent[i], p-cost[i])

def select_buildings(T, p):
    n = len(T)
    for i in range(n):
# origin index, h, a, b, koszt
        T[i] = (i, T[i][0], T[i][1], T[i][2], T[i][3])
    T.sort(key = lambda x: x[3])

    cost = [0]*n
    parent = [None]*n
    students = [0]*n

    for i in range(n):
        cost[i] = T[i][4]
        students[i] = T[i][1] * (T[i][3] - T[i][2])
        for j in range(i-1, -1, -1):
            if T[j][3] < T[i][2]: 
                parent[i] = j
                break

    DP = [[0 for _ in range(p+1)] for _ in range(n)]
    
    for i in range(p+1):
        if cost[0] <= i: DP[0][i] = students[0]

    for i in range(1, n):
        for j in range(p+1):
            DP[i][j] = DP[i-1][j]
            if parent[i] is not None and cost[i] <= j:
                DP[i][j] = max(DP[i][j], DP[parent[i]][j-cost[i]] + students[i])
            elif parent[i] is None and cost[i] <= j:
                DP[i][j] = max(DP[i][j], students[i])

    buildings = []
    f(DP, buildings, students, parent, cost, n-1, p)
    for i in range(len(buildings)):
        buildings[i] = T[buildings[i]][0]
    return sorted(buildings)

runtests( select_buildings )