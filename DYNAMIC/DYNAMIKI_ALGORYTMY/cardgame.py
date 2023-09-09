# f(a,b) -> zwraca krotke która zwraca 
# (max wartość osoby, która ma teraz ruch, max wartość do uzyskania 
# ruch po nas)
# z kart od a do b
# edge case: a==b: -> (T[a], 0)
#            a+1 == b -> (max(T[a], T[b]), min(T[a], T[b]))
# ogólnie: 
# f(a,b): if T[a] + f(a+1, b)[1] > T[b] + f(a, b-1)[1]
#            -> T[a] + f(a+1, b)[1]
#         else: -> T[b] + f(a, b-1)[1]

def cards( A ):
    
    n = len(A)
    DP = [[(0,0) for _ in range(n)] for __ in range(n) ]

    # edge cases
    for i in range(n):
        DP[i][i] = (A[i], 0)
    
    for i in range(n-1):
        DP[i][i+1] = (max(A[i], A[i+1]), min(A[i], A[i+1]))

    # general
    for a in range(n-2, -1, -1):
        for b in range(a+1, n):
            if A[a] + DP[a+1][b][1] > A[b] + DP[a][b-1][1]:
                DP[a][b] = (A[a] + DP[a+1][b][1], DP[a+1][b][0])
            else:
                DP[a][b] = (A[b] + DP[a][b-1][1], DP[a][b-1][0])

    return DP[0][n-1][0]