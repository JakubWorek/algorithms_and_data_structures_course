def minmax( T, k ):
    n = len( T )
    DP = [[0] * (k+1) for _ in range(n)]
    PSum = [0] *n
    
    PSum[0] = T[0]
    for i in range(1,n):
        PSum[i] = PSum[i-1] + T[i]

    for i in range(n):
        DP[i][1] = PSum[i]

    for i in range(n):
        for k1 in range(2, k+1):
            mini = inf
            for j in range(i):
                cost = max(PSum[i] - PSum[j], DP[j][k1 - 1])
                mini = min(mini, cost)
            DP[i][k1] = mini

    return DP[n-1][k]