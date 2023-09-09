# Mamy dwie tablice, A[n], B[n].
# Należy znaleźć najdłuższy wspólny podciąg 
# O(n^2)

'''
    F(i, j)={
        max(F(i-1,j), F(i, j-1), F(i-1, j-1)+1) 
        jeśli A[i] == B[j]
    } i elementów z A, j elementów z B
'''

def LCS(A,B):
    n = len(A)
    m = len(B)
    F = [[0] * m for _ in range(n)]

    F[0][0] = int(A[0] == B[0])
    # Fill the first row (compare the first value of the array A
    # with all the values from the B array)
    for j in range(1, m):
        if F[0][j - 1] or A[0] == B[j]:
            F[0][j] = 1
    # Fill the first column (compare the first value of the array B
    # with all the values from the A array)
    for i in range(1, n):
        if F[i - 1][0] or B[0] == A[i]:
            F[i][0] = 1
    # Fill the remaining array based on values previously calculated
    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    return F[n-1][m-1]