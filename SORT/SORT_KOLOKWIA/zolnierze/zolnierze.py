""" 
Algorytm na początek za pomocą funkcji select wyszukuje obecne indeksy elementów,
które w posortowanej tablicy znajdowały by się na indeksach p i q, następnie wykonuje 
dwa przejścia quicksorta by między p i q trafiły wszystkie potrzebne elementy i wykonujemy już
pełnego quicksorta na tym właśnie przedziale
"""

def partition(A,l,p):
    x = A[p]
    i = l-1
    for j in range(l,p):
        if A[j] <= x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[p]=A[p],A[i+1]
    return i+1

def quickselect(A,l,p,k):
    if l == p: return p

    q = partition(A,l,p)

    if q == k: return

    if q < k: return quickselect(A,q+1,p,k)
    else: return quickselect(A,l,q-1,k)

def zolnierze(T,p,q):
    n = len(T)
    quickselect(T, 0, n-1, p)
    quickselect(T,p,n-1,q)
    return T[p:q+1]

T = [10, 15, 34, 80, 97, 15, 24, 34, 11, 8, 2, 3]
print(zolnierze(T, 5, 8))
#print(T)