from zad9ktesty import runtests
from math import inf

# F(i,g,d) - i-ty pojazd, ile łącznie na pokładzie górnym, dolnym
# F(0,0,0) - start
# 2 warunki, czy pokłady nie są zapełnione, jeżeli obydwa pełne
# return 0
# else: sprawdzamy czy nie przekroczymy ilości na pokładzie
#
# max(f(i+1, g+T[i], d), f(i+1, g, d+T[i])) +1 i tyle bez zwracania
#
# i zwracanie tablicy z pokładu

def f(i, T, DP, g, d):
    if i >= len(T): return 0

    if DP[i][g][d] != -1: return DP[i][g][d]

    if T[i] > g and T[i] > d: 
        DP[i][g][d] = 0
        return 0

    if T[i] > g: DP[i][g][d] = f(i+1, T, DP, g, d-T[i]) + 1
    elif T[i] > d: DP[i][g][d] = f(i+1, T, DP, g-T[i], d) + 1
    else:
        w1 = f(i+1, T, DP, g, d-T[i])
        w2 = f(i+1, T, DP, g-T[i], d)
        DP[i][g][d] = max(w1, w2) + 1

    return DP[i][g][d]

def prom(P, g, d):
    DP = [[[-1 for _ in range(d+1)] for __ in range(g+1)] for ___ in range(len(P)) ]
    w = f(0, P, DP, g, d)
    
    i = 0
    l1 = g
    l2 = d
    sol1 = []
    sol2 = []

    while i<len(P) and (l1 >= P[i] or l2 >= P[i]):
        if P[i] > l1:
            w1 = 0
            w2 = 1
        elif P[i] > l2:
            w1 = 1
            w2 = 0
        else:
            w1 = f(i+1, P, DP, l1-P[i], l2)
            w2 = f(i+1, P, DP, l1, l2-P[i])

        if w1 > w2:
            sol1.append(i)
            l1 -= P[i]
        else:
            sol2.append(i)
            l2 -= P[i]
        i+=1

    if w-1 in sol1: return sol1
    else: return sol2

runtests ( prom )