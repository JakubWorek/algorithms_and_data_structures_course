from egzP1atesty import runtests 
from math import inf

# f(i) - minimalna ilość liter w alfabecie morsa potrzebna
# do zbudowania napisu długości i (i > 0)
# f(0) = 1
# f(i+1) = min(f(i - długość kodu + 1 ) + 1 dla dostępnych kodów morsa)

def titanic( W: str, M: list, D: list ):
    KOD_M: str = ''

    # konstruuję napis
    for litera in W:
        for lit, kod in M:
            if litera == lit:
                KOD_M += kod
                break

    n = len(KOD_M)
    DP = [inf for _ in range(n+1)]
    DP[0] = 0
    DP[1] = 1

    # tworzę słownik dostępnych kodów morsa
    SLOWNIK = []
    for i in D:
        SLOWNIK.append(M[i][1])
    
    # uzupełniam tablicę DP
    for i in range(1,n):
        for kod in SLOWNIK:
            if len(kod) <= i+1 and kod == KOD_M[i-len(kod)+1: i+1]:
                DP[i+1] = min(DP[i+1], DP[i-len(kod)+1] + 1)

    return DP[n]

runtests ( titanic, recursion=False )