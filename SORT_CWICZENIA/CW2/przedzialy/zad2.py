from zad2testy import runtests

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
    if( l<p ):
        q=partition(A,l,p)
        quicksort(A,l,q-1)
        quicksort(A,q+1,p)

def depth(A):
    # tu prosze wpisac wlasna implementacje
    n=len(A)
    quicksort(A,0,n-1)
    begin=[(A[i][0],i) for i in range(n)]
    end=[(A[i][1],i) for i in range(n)]

    quicksort(begin,0,n-1)
    quicksort(end,0,n-1)
    
    result=[0 for i in range(n)]

    for i in range(n):
        result[end[i][1]] += 1
        result[begin[i][1]] -= 1

    print(result)
    
    return max(result)


runtests( depth ) 
