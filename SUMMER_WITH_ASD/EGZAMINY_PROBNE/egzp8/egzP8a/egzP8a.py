from egzP8atesty import runtests
from math import inf
from bisect import bisect_right

def reklamy_n2(T, S, o):
    P=[]
    for i in range(len(T)):
        P.append((T[i][0], T[i][1], S[i]))
    P.append((inf, inf, 0))
    P.sort(key=lambda x: x[0])

    sol = 0
    for i in range(len(P)-1):
        start, end = P[i][0], P[i][1]
        for j in range(i+1, len(P)):
            start1, end1 = P[j][0], P[j][1]
            if start1 > end:
                sol = max(sol, P[i][2]+P[j][2])
    
    return sol

def reklamy_nlogn ( T, S, o ):
    n = len(T)
    P=[]
    for i in range(n):
        P.append((T[i][0], T[i][1], S[i]))
    P.sort(key=lambda x: x[0])

    M = [0 for _ in range(n)] # MAX
    M[n-1] = P[n-1][2]
    for i in range(n-2, -1, -1):
        M[i] = max(M[i+1], P[i][2])

    S = [P[i][0] for i in range(n)] # START

    sol = 0
    for i in range(n):
        end = P[i][1]
        ind = bisect_right(S, end, i+1)

        sec = 0
        if ind < n and S[ind] != end: sec = M[ind]
        sol = max(sol, P[i][2] + sec)

    return sol

runtests ( reklamy_n2, all_tests=True )