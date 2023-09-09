from math import inf

# Dla k początowych elementów będzie to ta liczba
# Dla pozostałych zwracamy T[i] + min i-k <= j < i f(j)
# Rozwiązaniem jest min z ostatnich k elementów

def ksuma( T, k ):
    n = len(T)
    DP = [inf for _ in range(n)]

    if k == 1: return sum(T)
    if k >= n: return min(T)

    # base case
    for i in range(k):
        DP[i] = T[i]

    # główne działania
    for i in range(k, n):
        for j in range(i-k, i):
            DP[i] = min(DP[i], T[i]+DP[j])

    mini = inf
    for i in range(n-k, n):
        mini = min(mini, DP[i])
    return mini