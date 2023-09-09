from zad1testy import runtests

def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_select(T, p, r, x):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if x == q:
        return T[x]
    elif x > q:
        return quick_select(T, q + 1, r, x)
    else:
        return quick_select(T, p, q - 1, x)

def linear(T):
    n = len(T)
    A = [0] * (n*n)
    idx = 0

    for i in range(n):
        for j in range(n):
            A[idx] = T[i][j]
            idx += 1
    
    return A

def Median(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    A = linear(T)
    interval = ((n*n)-n)//2 # np dla 4: przedział ma wartość 6

    # wybór elementów na miejsca:
    # pod przekątną
    quick_select(A, 0, n*n -1, interval)
    # nad przekątną
    quick_select(A, 0, n*n -1, n*n - interval)

    # umieszczanie elementów na przekątnej
    idx = interval
    for i in range(n):
        T[i][i] = A[idx]
        idx += 1

    # umieszczanie elementów pod główną przekątną
    idx = 0
    for i in range(n-1):
        for j in range(i+1, n):
            T[j][i] = A[idx]
            idx += 1

    # umieszczanie elementów nad główną przekątną
    idx = n*n - interval - 1
    for i in range(n-1):
        for j in range(i+1, n):
            T[i][j] = A[idx]
            idx += 1

    return T

runtests( Median ) 
