def get_split_indices(P):
    res = []
    t = len(P[0]) - 1
    j = len(P) - 1
    
    while j is not None:
        res.append(j)
        j = P[j][t]
        t -= 1
        
    res.reverse()
    return res


def split_array(A, S):
    res = []
    i = 0
    
    for j in S:
        res.append(A[i:j+1])
        i = j + 1
        
    return res


def find_division(A: 'sequence of numbers to split', k: 'number of splits'):
    if k == 0: return 0
    
    n = len(A)
    inf = float('inf')
    F = [[0] * (k + 1) for _ in range(n)]
    P = [[None] * (k + 1) for _ in range(n)]
    
    # Fill the column for k = 1
    F[0][1] = A[0]
    for i in range(1, n):
        F[i][1] = F[i - 1][1] + A[i]
    
    # Sotore sums of values from 0 index to 'i' index
    S = [0] * n
    S[0] = A[0]
    for i in range(1, n):
        S[i] = S[i - 1] + A[i]
        
    # Find the maximum value of the minimum split for each k value based
    # upon results for the previous subsequences and k values
    for t in range(2, k + 1):
        # We will consider all numbers up to a number at 'i' index (inclusive)
        for i in range(t - 1, n):
            # Loop over an index of the last number which will be included
            # in the first t - 1 splits
            for j in range(t - 2, i):
                curr_min = min(F[j][t - 1], S[i] - S[j])
                if curr_min > F[i][t]:
                    F[i][t] = curr_min
                    P[i][t] = j
    
    return F[n - 1][k], split_array(A, get_split_indices(P))

A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3
print(find_division(A, k))

A=[644,909,656,707,1000,182,-90,621,842,947,509,642,102,522,649,195,284,116,459,335,771,750, 495,268,576]
#print(find_division(A,5))

A = [1,2,3,4]
k = 3
print(find_division(A, k))