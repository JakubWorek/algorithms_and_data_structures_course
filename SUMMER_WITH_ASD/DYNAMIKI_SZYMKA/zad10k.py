from zad10ktesty import runtests
from math import inf

# f(a) = min(f(a-1^2), f(a-2^2), f(a-3^2), ...)
# f(a) - najmniejsza ilosc dywanow aby osiągnać a metrów kwadratowych

def dywany ( N ):
    #Tutaj proszę wpisać własną implementację
    DP = [inf for _ in range(N+1)]
    parents = [-1 for _ in range(N+1)]

    DP[0] = 0
    DP[1] = 1
    parents[1] = 1

    for a in range(2, N+1):
        i = 1
        if i*i == a: 
            DP[a] = 1
            parents[a] = int(i ** (1/2))
        while a - i*i >= 0:
            if DP[a - i*i] + 1 < DP[a]:
                DP[a] = DP[a - i*i] + 1
                parents[a] = i 
            i+=1

    indx = N
    sol = []
    while parents[indx] != -1:
        sol.append(parents[indx])
        indx = indx - parents[indx] ** 2

    return sol


runtests( dywany )

