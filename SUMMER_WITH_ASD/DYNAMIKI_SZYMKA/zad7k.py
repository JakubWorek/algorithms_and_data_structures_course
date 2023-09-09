from zad7ktesty import runtests 

def korzen (T, n, m, row, col):
    if(row >= 0 and row <= n-1 and col >= 0 and col <= m-1\
        and T[row][col] != 0):
        res = T[row][col]
        T[row][col] = 0
        res += (korzen(T, n, m, row+1, col)\
            + korzen(T, n, m, row-1, col)\
            + korzen(T, n, m, row, col+1)\
            + korzen(T, n, m, row, col-1))
        return res
    return 0

def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B + 1)] for i in range(n)]

    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    return F[n - 1][B]

def ogrodnik (T, D, Z, l):
    n = len(T)
    m = len(T[0])
    
    K = []

    for i in D:
        K.append(korzen(T, n, m, 0, i))

    # i rozwiązujemy problem plecakowy dla
    # K - waga
    # Z - zysk
    # l - max waga

    return knapsack(K, Z, l)


runtests( ogrodnik, all_tests=True )
