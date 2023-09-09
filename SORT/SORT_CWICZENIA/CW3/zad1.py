# Quickort z log n dodatkowej pamięci

def partition(A,l,p):
    x=A[p]
    i=l-1
    for j in range(l,p):
        if( A[j]<=x ):
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

A=[124,25,3257,124698,143,6413,1469]
quicksort(A,0,len(A)-1)
print(A)