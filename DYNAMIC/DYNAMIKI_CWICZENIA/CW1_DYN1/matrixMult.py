# Matrix chain multiplication

# f(i,j) - min koszt mnozenia od indeksu i do indeksu j
# f(i, i+1) = Mi * M(i+1)
# f(i, i) = 0, koszt mnozenia od indeksu i do indeksu i wynosi 0
# f(i, j) = min(f(i,k)+f(k+1,j) + d(i-1)*d(k)*d(j))

# tablica z wymiarami macierzy
# T = [(5, 4), (4, 6), (6, 2), (2, 7)]
# koszt mnozenia M0 i M1 to 5*4*6

# o(n^3)

def multiply(M1, M2):
    return M1[0] * M1[1] * M2[1]

def matrixMultiplication(T):
    n = len(T)
    dp = [[float("inf")] * n for _ in range(n)]
    m_size = [[(None, None)] * n for _ in range(n)]      # matrixes size

    for i in range(n):                                   # f(i, i) = 0, koszt mnozenia od indeksu i do indeksu i wynosi 0
        dp[i][i] = 0
        m_size[i][i] = (T[i][0], T[i][1])
    for i in range(n-1):                                 # f(i, i+1) = Mi * M(i+1)
        dp[i][i+1] = multiply(T[i], T[i+1])              # uzupelniam dodatkowo tablice m_size
        m_size[i][i+1] = (T[i][0], T[i+1][1])

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            for k in range(i, j):
                if dp[i][j] > dp[i][k] + dp[k+1][j] + multiply(m_size[i][k], m_size[k+1][j]):
                    dp[i][j] = dp[i][k] + dp[k+1][j] + multiply(m_size[i][k], m_size[k+1][j])   # aktualizuje tablice dp
                    m_size[i][j] = (m_size[i][k][0], m_size[k+1][j][1])                         # aktualizuje tablice m_size

T = [(5, 4), (4, 6), (6, 2), (2, 7)]
matrixMultiplication(T)