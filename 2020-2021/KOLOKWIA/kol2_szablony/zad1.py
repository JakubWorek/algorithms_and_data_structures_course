from zad1testy import runtests

# f(building, cost) - maksymalna liczba studentow, ktore moga mieszkac w budynku
# od 0 do 'i', ktore na siebie nie nachodza i kosztuja najwyzej 'cost'


def f(DP,buildings, students, parent, cost, i, p):
    if i <0: return buildings
    if i == 0:
        if p>=cost[0]:
            buildings.append(0)
        return buildings
    if DP[i-1][p] == DP[i][p]:
        return f(DP, buildings, students, parent, cost, i-1, p)
    buildings.append(i)
    return f(DP, buildings, students, parent, cost, parent[i], p-cost[i])

def prev(T, i):
    b = 0
    e = i
    while b <= e:
        mid = (b+e)//2
        if T[mid][2] >= T[i][1]:
            e = mid-1
        else:
            b = mid+1
    return e

def select_buildings(T, p):
    n = len(T)
    for i in range(n):
                # h,        a,      b,      koszt, origin index
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    T.sort(key = lambda x: x[2])

    cost = [0]*n
    parent = [0]*n
    students = [0]*n

    for i in range(n):
        cost[i] = T[i][3]
        students[i] = T[i][0] * (T[i][2] - T[i][1])
        parent[i] = prev(T,i)

    DP = [[0 for _ in range(p+1)] for _ in range(n)]
    
    for i in range(p+1):
        if cost[0] <= i: DP[0][i] = students[0]

    for i in range(1, n):
        for j in range(p+1):
            DP[i][j] = DP[i-1][j]
            if cost[i] <= j:
                DP[i][j] = max(DP[i][j], DP[parent[i]][j-cost[i]] + students[i])

    buildings = []
    acc = p
    total = DP[n-1][p]
    while DP[n-1][acc-1] == total: acc-=1
    f(DP, buildings, students, parent, cost, n-1, acc)
    for i in range(len(buildings)):
        buildings[i] = T[buildings[i]][4]
    return sorted(buildings)

runtests( select_buildings ) 
