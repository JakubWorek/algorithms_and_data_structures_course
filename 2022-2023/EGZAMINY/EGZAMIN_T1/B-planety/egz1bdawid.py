from egz1btesty import runtests
from math import inf


def planets( D, C, T, E ):
    n = len(D)
    F = [[float("inf")]*(E+1) for _ in range(n)]

    for t in range(E+1):
        F[0][t] = t*C[0]

    for i in range(n-1):
        for t in range(E+1):
            # mam paliwo
            dist = D[i+1]-D[i]
            if t >= dist:
                F[i+1][t-dist] = min(F[i+1][t-dist], F[i][t])
            else:
                for after_tank in range(E+1):
                    F[i+1][after_tank] = min(F[i+1][after_tank], F[i][t] + (after_tank - (t-dist))*C[i])

            #mam teleport
            if t == 0 and T[i][0] != i:
                F[T[i][0]][0] = min(F[T[i][0]][0], F[i][t]+T[i][1])

    #print(F, sep="\n")
    #input()

    return min(F[n-1])

runtests( planets, all_tests = True )