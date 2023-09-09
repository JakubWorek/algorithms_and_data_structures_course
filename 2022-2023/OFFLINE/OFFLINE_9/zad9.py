# Jakub Worek 19.06.2023 - 25.06.2023
#
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

from zad9testy import runtests

def min_cost( O, C, T, L ):
    n = len(O)
    DP = [[float("inf")] * 2 for _ in range(n+2)]
    DP[0][0] = 0
    DP[0][1] = 0

    P = [(0, 0)]
    for i in range(n):
        P.append((O[i], C[i]))

    P.append((L, 0))

    P.sort(key=lambda x: x[0])

    for i in range(n+2):
        for j in range(i+1, n+2):
            if P[i][0] + T >= P[j][0]:
                DP[j][1] = min(DP[j][1], DP[i][1] + P[j][1])
                DP[j][0] = min(DP[j][0], DP[i][0] + P[j][1])
            if P[i][0] + 2*T >= P[j][0]:
                DP[j][1] = min(DP[j][1], DP[i][0] + P[j][1])
            else: break

    return min(DP[-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
