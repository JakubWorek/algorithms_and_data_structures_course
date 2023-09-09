# Najdłuższy podciąg rosnący.

'''
    f(i) - długość najdłuższego konczącego się na A[i]
    f(i)={
        f(j)+1, j<i
    }
'''

def lis(A):
    n = len(A)
    F = [1]*n
    for i in range(n):
        for j in range(i):
            if A[i]>=A[j]:
                F[i] = max(F[i], F[j]+1)
    return max(F)

A = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
print(lis(A))