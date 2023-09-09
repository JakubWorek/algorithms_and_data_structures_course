from zad11ktesty import runtests

# f(i, p1, p2) - ity rozpatrywany element, pokład 1 i 2 i dodajemy
# f(i, p1, p2) = min(f(i+1, p1+t[i], p2), f(i+1, p1, p2+t[i]))

# ale dla złożoności O(nS) gdzie S to sum(T)
# będziemy używali samego p1, parametr p2 obliczymy S-p1

def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    S = sum(T)

    DP = [[False for _ in range(S+1)] for __ in range(n)]
    
    # base case - pierwszy przedmiot
    DP[0][T[0]] = True

    for i in range(1, n):
        for halfWeight in range(S+1):
            if not DP[i][halfWeight]:
                DP[i][halfWeight] = DP[i-1][halfWeight]
            if DP[i-1][halfWeight]:
                DP[i][halfWeight + T[i]] = True

    minDiff = S
    for halfWeight1 in range(S+1):
        halfWeight2 = S-halfWeight1
        if DP[n-1][halfWeight1] and abs(halfWeight1 - halfWeight2) < minDiff:
            minDiff = abs(halfWeight1 - halfWeight2)

    return minDiff

runtests ( kontenerowiec )
    