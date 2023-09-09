from zad3testy import runtests
from math import inf


def iamlate(T, V, q, l):
    #tu prosze wpisac wlasna implementacje
    T.append(l)
    V.append(0)
    n = len(T)

    DP = [[inf for _ in range(q+1)] for _ in range(n)]
    

    new_fuel = min(V[0], q)
    DP[0][new_fuel] = 0

    Parent = [[[-1,-1] for _ in range(q+1)] for _ in range(n)]

    for station in range(n):
        for fuel in range(q+1):
            if DP[station][fuel] != inf:
                # możemy jechać dopóki T[station+distance] - T[station] <= fuel
                distance = 1
                while station + distance < n and T[station+distance] - T[station] <= fuel:
                    new_fuel = min(q, fuel-(T[station+distance]-T[station]) + V[station+distance])
                    if DP[station+distance][new_fuel] > 1 + DP[station][fuel]:
                        DP[station+distance][new_fuel] = 1 + DP[station][fuel]
                        Parent[station+distance][new_fuel][0] = station
                        Parent[station+distance][new_fuel][1] = fuel
                    distance += 1

    #print(DP)

    minDist = inf
    fuel = 0
    for i in range(q+1):
        if minDist > DP[-1][i]:
            minDist = DP[-1][i]
            fuel = i
    
    if minDist == inf: return []
    
    station,fuel = Parent[-1][fuel]
    sol = []
    while station != -1:
        sol.append(station)
        station, fuel = Parent[station][fuel]

    return list(reversed(sol))

runtests( iamlate )
