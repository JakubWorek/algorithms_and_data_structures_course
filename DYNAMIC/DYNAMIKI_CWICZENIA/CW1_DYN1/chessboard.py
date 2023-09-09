# Dana jest szachownica A o wymiarach nxn. Zawiera liczby wymierne.
# Z pola (1,1) na pole (n,n) korzystając z ruchów w dół i prawo 
# po minimalnym koszcie.

'''
    f(i,j) = min(f(i-1, j), f(i, j-1))
    f(0,0) = 0
'''

def min_cost(A: 'matrix with costs', M: 'number of rows', N: 'number of columns'):
    F = [[0] * N for _ in range(M)]
    F[0][0] = A[0][0]
    
    # Fill the first column
    for i in range(1, M):
        F[i][0] = A[i][0] + F[i - 1][0]
    # Fill the first row
    for j in range(1, N):
        F[0][j] = A[0][j] + F[0][j - 1]
    # Fill the remaining matrix
    for i in range(1, M):
        for j in range(1, N):
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + A[i][j]
        
    return F[M - 1][N - 1], F