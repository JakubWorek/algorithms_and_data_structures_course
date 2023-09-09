from egzP4atesty import runtests 
from math import inf

def f(T, DP, i):
    if i == 0: return 1
    if DP[i] != -1: return DP[i]

    maxx = 1
    for j in range(i):
        if T[j] < T[i]:
            maxx = max(maxx, f(T, DP, j) +1)
    DP[i] = maxx
    return DP[i]

def lis(T):
    T.append(inf)
    DP = [-1 for _ in range(len(T))]
    return f(T, DP, len(T)-1)-1


def mosty ( T ):
    #tutaj proszę wpisać własną implementację 
    T.sort(key = lambda x: (x[0], x[1]))
    T2 = [T[i][1] for i in range(len(T))]

    return lis(T2)

runtests ( mosty, all_tests=False )