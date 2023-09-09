from zad1ktesty import runtests

# f(a,b) roznica zer i jedynek w ciagu od a bo b

def roznica( S ):
    #Tutaj proszę wpisać własną implementację
    if '0' not in S: return -1
    n = len( S )
    DP = [ [0 for _ in range(n)] for __ in range(n) ]

    for a in range(n):
        for b in range(a+1,n):
            if S[b] == '0': ile = 1
            else: ile = -1
            DP[a][b] = max(DP[a][b], DP[a][b-1] + ile)
    
    maxi = -n
    for a in range(n):
        for b in range(n):
            maxi = max(maxi, DP[a][b])
    return maxi

runtests ( roznica )