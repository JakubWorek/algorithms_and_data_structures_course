def count_removed_bricks(A: 'array of bricks spans'):
    n = len(A)
    F = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            # Check if a brick A[i] can fall on a brick A[j]
            if can_fall(A[i], A[j]):
                F[i] = max(F[i], F[j] + 1)
                
    print(F)
                
    return n - max(F)


def can_fall(a, b):
    return a[0] >= b[0] and a[1] <= b[1]