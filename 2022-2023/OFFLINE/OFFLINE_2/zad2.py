# Jakub Worek 13.03.2023-18.03.2023                                                     #
#                                                                                       #
# Dowód poprawności:                                                                    #
# Szukamy największej sumy metrów sześciennych śniegu możliwej do zebrania.             #
# W tym celu sortuje tablice nierosnąco i uwzględniając topnienie śniegu zliczam sumę.  #
# Mogę to zrobić, ponieważ kolejność zbierania tej maksymalnej sumy                     #
#   nie ma znaczenia, i zawsze da się ją zebrać.                                        #
#                                                                                       #
# Przykład:                                                                             #
# [1,7,3,4,1] -> [7,4,3 |,1,1], maksymalna suma uwzględniając topnienie: 11             #
# [2,1,3,7,6,9,4,2,0] -> [9,7,6,4 |,3,2,2,1,0], max suma: 9+6+4+1=20                    #
#   w powyższym przypadku są 2 możliwości zebrania max sumy: 4,9,6,7 albo 7,6,9,4       #
#                                                                                       #
# Złożoność:                                                                            #
# O(nlogn)                                                                              #
#                                                                                       #
#########################################################################################

from zad2testy import runtests

def partition(A,l,p):
    x=A[p]
    i=l-1
    for j in range(l,p):
        if( A[j]>x ):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[p]=A[p],A[i+1]
    return i+1


def quicksort(A,l,p):
    if(len(A)==1): return A
    while( l<p ):
        q=partition(A,l,p)
        if(q-l<p-q):
            quicksort(A,l,q-1)
            l=q+1
        else:
            quicksort(A,q+1,p)
            p=q-1


def snow( S ):
    # tu prosze wpisac wlasna implementacje
    n=len(S)
    quicksort(S,0,n-1)
    j=0
    suma=0

    while(S[j]-j>0):
        suma+=(S[j]-j)
        j+=1

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
