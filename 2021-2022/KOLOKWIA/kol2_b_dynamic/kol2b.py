from kol2btesty import runtests
from math import inf

# f(i,w) - minimalnny koszt dotarcia do i-tego miasta pod warunkiem w
# f(0) = 0
# w = 0 -> nie użyliśmy bonusu
# w = 1 -> użyliśmy bonus
#
# f(i,0) = min(f(i-k,0) + C[i] dla O[i]-O[i-k] <= T )
# f(i,1) = min(f(i-k,1) + C[i] dla O[i]-O[i-k] <= T,
#            f(i-k,0) + C[i] dla O[i]-O[i-k] <= 2*T )
#
# Złożoność O(n^2)

def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje
    OC = []
    OC.append((0,0))
    OC.append((L,0))
    for o, c in zip(O, C):
        OC.append((o,c))
    OC.sort(key=lambda x: x[0])
    n = len(OC)
    
    DP = [[inf]*2 for _ in range(n)]
    DP[0][0], DP[0][1] = 0, 0

    for miasto in range(1,n):
        for postoj in range(miasto-1, -1, -1):
            if OC[miasto][0] - OC[postoj][0] > 2*T: break
            if OC[miasto][0] - OC[postoj][0] <= T:
                DP[miasto][0] = min(DP[miasto][0], DP[postoj][0] + OC[miasto][1])
                DP[miasto][1] = min(DP[miasto][1], DP[postoj][1] + OC[miasto][1])
            else:
                DP[miasto][1] = min(DP[miasto][1], DP[postoj][0] + OC[miasto][1])
    
    return min(DP[-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
