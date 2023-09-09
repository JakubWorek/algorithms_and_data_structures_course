# Jakub Worek 13.07.2023
#
# Opis:
# Przechodzę po kolejnych planetach, updatuje koszt dotarcia na
# planetę i z poprzednich j planet z uwzględnieniem, że 
# jeżeli jestem na planecie j i mogę z niej skoczyc na planete i
# to ten skok odnotowyję
#
# Złożoność:
# O(n*E)

from egz1btesty import runtests
from math import inf

def planets( D, C, T, E ):
    n = len(D)
    DP = [[inf for _ in range(E+1)] for __ in range(n)]

    # base case: tankowanie na 0 planecie i teleportacja z 0 planety
    for i in range(E+1):
        DP[0][i] = C[0]*i
    
    DP[T[0][0]][0] = min(DP[T[0][0]][0], DP[0][0] + T[0][1])

    for i in range(1, n):
        fuel_cost = C[i]
        distance = D[i] - D[i-1]

        # przelot
        for e in range(E+1):
            if e + distance <= E:
                DP[i][e] = min(DP[i][e], DP[i-1][e+distance])

        # dotankowywanie
        for e in range(1, E+1):
            DP[i][e] = min(DP[i][e], DP[i][e-1] + fuel_cost)

        # teleportacja
        dest, cost = T[i]
        DP[dest][0] = min(DP[dest][0], DP[i][0] + cost)
    
    return min(DP[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
