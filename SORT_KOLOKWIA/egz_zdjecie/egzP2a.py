from egzP2atesty import runtests 

def partition(T,indeksy,p,r):
    pivot = T[indeksy[r]][1]
    i=p-1
    for j in range(p,r):
        if T[indeksy[j]][1] > pivot:
            i+=1
            T[indeksy[i]], T[indeksy[j]] = T[indeksy[j]], T[indeksy[i]]
    T[indeksy[i+1]], T[indeksy[r]] = T[indeksy[r]], T[indeksy[i+1]]
    return i+1


def select(T, indeksy, p, k, r):
    if p<r:
        q=partition(T, indeksy, p, r)
        if q<k:
            select(T, indeksy, q+1, k, r)
        elif q>k:
            select(T,indeksy,p,k,q-1)
    return


def zdjecie(T, m, k):
    n=len(T)

    start = [0 for _ in range(m)]
    end = [0 for _ in range(m)]

    aktEnd = -1
    aktWidth = k+m-1

    for i in range(m):
        start[i] = aktEnd+1
        aktEnd += aktWidth
        end[i] = aktEnd
        aktWidth -= 1

    indeksy = [0 for _ in range(n)]
    osoba = 0
    column = 0
    row = 0

    # nadajemy osobom nowe indeksy
    while osoba < n:
        if start[row] + column <= end[row]:
            indeksy[start[row] + column] = osoba
            osoba += 1
        row += 1
        if row >= m:
            row = 0
            column +=1

    # ustawiamy według wzrostu od przedostatniego rzędu
    lastEnd = end[m-1]
    for i in range(m-2,-1,-1):
        select(T, indeksy, 0, end[i], lastEnd)
        lastEnd = end[i]-1

    return None

runtests ( zdjecie, all_tests=False )