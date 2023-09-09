# Jakub Worek 30.03.2023
#
# Idąc po wycinkach z tablicy długości p algorytm znajduje k-ty najwiekszy element i je sumuje
# Do znajdywania k-tego najwiekszego elementu wykorzystuję quickselect
#
# Złożoność:
# O(np), ponieważ dla każdego przedziału wykonuję quickselecta z p elementów

from kol1testy import runtests

def partition(A,l,p):
    x=A[p]
    i=l-1
    for j in range(l,p):
        if(A[j]>x):
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[p]=A[p],A[i+1]
    return i+1


def quickselect(A,l,p,k):
    if( l==p ): return A[l]

    q=partition(A,l,p)

    if(q==k): return A[q]

    if( q<k ): 
        return quickselect(A,q+1,p,k)
    else:
        return quickselect(A,l,q-1,k)

def quicksort(A,l,p):
    if(len(A)==1): return 
    if( l<p ):
        q=partition(A,l,p)
        quicksort(A,l,q-1)
        quicksort(A,q+1,p)


def ksum(T, k, p):
    n=len(T)
    suma=0
    for i in range(0,n-p+1):
        kopia=T[i:i+p]
        suma+=quickselect(kopia,0,p-1,k-1)
        #print(T)
        #print(suma)
    
    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
