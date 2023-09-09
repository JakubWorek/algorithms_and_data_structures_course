from egzP5atesty import runtests 

# Podproblem:
# Minimalna wartość z przedziału (a,b)
# F(a,b) -> jakaś liczba, minimalna 
#  a == b -> T[a]
#  else -> min (T[b], f(a,b-1))
# O(n^2)

# Główny problem:
# Bruteforce z wykorzystaniem powyższej tablicy

# Złożoność: O(n^2)

def f(T, DP, a, b):
    if a == b: return T[a]
    if DP[a][b] != -1: return DP[a][b]
    DP[a][b] = min(f(T, DP, a, b-1), T[b])
    return DP[a][b]

def inwestor ( T ):
    n = len(T)
    DP = [[-1 for _ in range(n)] for _ in range(n)]
    maxi = 0
    for i in range(n):
        for j in range(i, n):
            maxi = max(maxi, (j-i+1)*f(T,DP,i,j))
    return maxi

runtests ( inwestor, all_tests=True )