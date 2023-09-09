from egzP2atesty import runtests 

def zdjecie(T, m, k):
    n = len(T)
    START = [0 for _ in range(m)]
    END = [0 for _ in range(m)]

    aktEND = -1
    aktWIDTH = m+k-1

    for i in range(m):
        START[i] = aktEND+1
        aktEND += aktWIDTH
        END[i] = aktEND
        aktWIDTH -= 1

    IND = [0 for _ in range(n)]
    items = 0
    col = 0
    row = 0
    while items < n:
        if START[row] + col <= END[row]:
            IND[START[row] + col] = items
            items += 1
        row += 1
        if row >= m:
            row = 0
            col += 1
    
    lastEND = END[m-1]
    for i in range(m-2, -1, -1):
        quickselect(T, IND, 0, END[i], lastEND)
        lastEND = END[i]-1

    return None

def partition(T, IND, p, r):
    pivot = T[IND[r]][1]
    i = p-1
    for j in range(p, r):
        if T[IND[j]][1] >= pivot:
            i += 1
            T[IND[j]], T[IND[i]] = T[IND[i]], T[IND[j]]
    T[IND[i+1]], T[IND[r]] = T[IND[r]], T[IND[i+1]]
    return i+1


def quickselect(T, IND, p, k, r):
    if p < r:
        q = partition(T, IND, p, r)
        if q>k:
            quickselect(T, IND, p, k, q-1)
        elif q<k:
            quickselect(T, IND, q+1, k, r)
    return


runtests ( zdjecie, all_tests=False )