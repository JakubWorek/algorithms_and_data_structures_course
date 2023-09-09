from zad1testy import runtests

def mr( X ):
    """tu prosze wpisac wlasna implementacje"""
    n = len( X )
    # Lis od przodu
    F_FWD = [1]*n
    P_FWD = [-1]*n

    for i in range(1,n):
        for j in range(i):
            if X[i] < X[j] and F_FWD[i] < F_FWD[j] + 1:
                F_FWD[i] = F_FWD[j] + 1
                P_FWD[i] = j

    # Lis od tyłu
    F_BCK = [1]*n
    P_BCK = [-1]*n

    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if X[i] < X[j] and F_BCK[i] < F_BCK[j] + 1:
                F_BCK[i] = F_BCK[j] + 1
                P_BCK[i] = j

    # Szukamy maxa
    _max = 0
    idx = 0

    for i in range(n):
        if F_FWD[i] + F_BCK[i] - 1 > _max:
            _max = F_FWD[i] + F_BCK[i] -1
            idx = i

    # Budujemy odpowiedź
    if idx == 0 or idx == n-1: return X

    sol = [0]*_max
    index = F_FWD[idx] - 1
    sol[index] = X[idx]
    i, j = P_FWD[idx], P_BCK[idx]
    i1, j1 = index - 1, index + 1

    while P_FWD[i] != -1:
        sol[i1] = X[i]
        i1 -= 1
        i = P_FWD[i]

    while P_BCK[j] != -1:
        sol[j1] = X[j]
        j1 += 1
        j = P_BCK[j]

    sol[0] = X[i]
    sol[_max-1] = X[j]
    return sol


runtests( mr )