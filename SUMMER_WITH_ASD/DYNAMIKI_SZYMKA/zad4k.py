from zad4ktesty import runtests
from math import inf

# Klasyczny spacer po szachownicy w prawo i dół

def falisz ( T ):
    n = len(T)
    DP = [[0]*n for _ in range(n)]

    # base case
    DP[0][0] = T[0][0]
    for i in range(1, n):
        DP[i][0] = T[i][0] + DP[i-1][0]
        DP[0][i] = T[0][i] + DP[0][i-1]

    for i in range(1,n):
        for j in range(1,n):
            DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + T[i][j]

    return DP[n-1][n-1]

runtests ( falisz )
