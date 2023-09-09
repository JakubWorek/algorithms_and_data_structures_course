def max_profit(T: 'values of trees'):
    if not T: return 0
    if len(T) <= 2: return max(T)
    
    n = len(T)
    m = int(n / 2 + 1.5)  # Max number of trees that can be cut
    F = [[0] * m for _ in range(n)]
    
    # Fill the first two rows of an array as there is only one choice
    # (from the first two trees a lumberjack will choose only the one
    # tree of the greater profit as he cannot cut both threes)
    for j in range(1, m):
        F[0][j] = T[0] 
    
    curr_max = max(T[0], T[1])
    for j in range(1, m):
        F[1][j] = curr_max
        
    # Choose the best profit for the remaining trees
    for i in range(2, n):
        for j in range(1, m):
            F[i][j] = max(F[i - 2][j - 1] + T[i], F[i - 1][j])
            
    #print(*F, sep='\n')
    
    return F[n - 1][m - 1]

T = [1, 8, 3, 4, 5, 1, 2]
print(max_profit(T)) #15
T = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
print(max_profit(T)) #14
T = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
print(max_profit(T)) #23