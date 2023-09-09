# węgiel
from egz2atesty import runtests

def coal( A, T ):
    n = len( A )
    sklady = [T for _ in range(n)]
    ktory = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sklady[j] >= A[i]:
                sklady[j] -= A[i]
                ktory[i] = j
                break

    return ktory[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
