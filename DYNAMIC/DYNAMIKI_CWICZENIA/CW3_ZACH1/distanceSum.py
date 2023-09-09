# Wybieramy medianę z tablicy
def distSum(T):
    n = len(T)
    if n % 2 == 1: return T[n // 2]
    upper = n // 2
    lower = n // 2 - 1
    return (T[lower] + T[upper]) / 2

def find_x(A):
    return A[len(A) // 2]

A = [1, 5, 6, 6, 8]
print(distSum(A))