from zad6ktesty import runtests 

# f(i) - nasz ciąg do i-tego i liczba sposobow na zaszyfrowanie
#
# f(i) bez edge casów f(i-1) + f(i-2)
# S[i-1] == 3 -> f(i-1) samo
# i tak samo dla >=27
# i 0 0 też odpada

def haslo ( S ):
    n = len( S )
    DP = [0 for _ in range(n)]

    # edge cases
    DP[0] = 1
    if S[1] != '0': DP[1] = DP[0]
    if S[1] != '0' and int(S[0:2]) <= 26: DP[1] = 2

    # general
    for i in range(2,n):
        if S[i] != '0': DP[i] += DP[i-1]
        if S[i-1] != '0' and int(S[i-1:i+1]) <= 26: DP[i] += DP[i-2]

    return DP[n-1]

runtests ( haslo )