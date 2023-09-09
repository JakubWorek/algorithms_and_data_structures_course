# Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm, który sprawdza,
# czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T .

'''
f(i,v)={
    True gdy f(i+1,T) or f(i+1, T-A[i])
    False wpp
}

f(i,0) = True - warunek początkowy
f(i, v) = False gdy v<0

'''

def subSum(A, T):
    n = len(A)
    DP = [[0 for _ in range(T+1)] for __ in range(n)]
    for i in range(n):
        DP[i][0] = 1
    DP[0][A[0]] = 1
    for i in range(1, n):
        for j in range(1, T+1):
            if A[i] <= j:
                DP[i][j] = DP[i-1][j] or DP[i-1][j-A[i]]
            else: 
                DP[i][j] = DP[i-1][j]
    return DP[n-1][T]

A = [4, 4, 1, 0, 7, 1]
T = 10
print(subSum(A, T))

