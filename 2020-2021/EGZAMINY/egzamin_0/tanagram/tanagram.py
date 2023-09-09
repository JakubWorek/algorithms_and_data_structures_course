from zad1testy import runtests

def countingSort(T, k):
    C = [0]*k
    B = [0]*len(T)
    for i in range(len(T)):
        C[T[i][0]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(T)-1, -1, -1):
        C[T[i][0]] -= 1
        B[C[T[i][0]]] = T[i]
    
    return B

def tanagram(x, y, t):
    n = len(x)
    A, B = [], []

    for i in range(n):
        A.append([ord(x[i]) - ord("a"), i])
        B.append([ord(y[i]) - ord("a"), i])
    
    A = countingSort(A, 26)
    B = countingSort(B, 26)

    for i in range(n):
        if abs(A[i][1] - B[i][1]) > t: return False
    
    return True


runtests(tanagram)