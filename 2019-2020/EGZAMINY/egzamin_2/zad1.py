from zad1testy import runtests
from math import inf

def zbigniew1(A):
    n = len(A)
    max_e = sum(A)+1
    min_jumps = [[float("inf")] * n for _ in range(max_e)]
    min_jumps[A[0]][0] = 0

    for i in range(n):
        for e in range(1, max_e):
            if min_jumps[e][i] != float("inf"):
                pointer = i + 1
                while pointer < n and e - (pointer-i) >= 0:
                    curr_energy = e + A[pointer] - (pointer-i)
                    min_jumps[curr_energy][pointer] =\
                        min(min_jumps[curr_energy][pointer], min_jumps[e][i]+1)
                    pointer += 1

    jumps = float("inf")
    for i in range(max_e):
        jumps = min(jumps, min_jumps[i][n-1])
    return jumps

def zbigniew( A ):
    count = 0
    for i in range(len(A)):
        count += A[i]
    DP = [[inf] * (count + 1) for _ in range(len(A))]
    DP[0][A[0]] = 0
    for i in range(len(A)):
        for j in range(count):
            if DP[i][j] != inf:
                k = i + 1
                while k < len(A) and j >= k - i:
                    index = i + j + A[k] - k
                    DP[k][index] = min(DP[k][index], DP[i][j] + 1)
                    k += 1
    return min(DP[-1])

runtests( zbigniew ) 
