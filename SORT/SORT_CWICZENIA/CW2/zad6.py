# Dany jest ciąg przedziałów domkniętych [a1, b1], ..., [an, bn]. Proszę zapropnować algorytm, który
# znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej innych przedziałów.

def partition(A,l,p,ind):
    x=A[p][ind]
    i=l-1
    for j in range(l,p):
        if( A[j][ind]<=x ):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[p]=A[p],A[i+1]
    return i+1

def quicksort(A,l,p,ind):
    if(len(A)==1): return A
    if( l<p ):
        q=partition(A,l,p,ind)
        quicksort(A,l,q-1,ind)
        quicksort(A,q+1,p,ind)

def most_intervals(A):
    quicksort(A,0,len(A)-1,0)
    for i in range(len(A)):
        A[i]=(A[i][0],A[i][1],i)
    print(A)

    quicksort(A,0,len(A)-1,1)
    for i in range(len(A)):
        A[i]=(A[i][0],A[i][1],A[i][2],i)
    print(A)

    max_interval = 0
    max_ind=0
    for i in range(len(A)):
        if A[i][3]-A[i][2] > max_interval:
            max_interval = A[i][3]-A[i][2]
            max_ind = i
    
    return T[max_ind][0],T[max_ind][1]


T = [(4, 8), (5, 9), (1, 2), (1, 3), (2, 8), (3, 7), (4, 6), (8, 9), (6, 10), (6, 11), (9, 14), (11, 16), (3, 4)]
print(most_intervals(T))