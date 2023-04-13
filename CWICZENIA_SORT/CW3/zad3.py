def partition(A,l,p):
    x=A[p]
    i=l-1
    for j in range(l,p):
        if( A[j]<=x ):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[p]=A[p],A[i+1]
    return i+1

def quicksort(A):
    stack=[]
    stack.append((0,len(A)-1))
    while(stack):
        l,p=stack.pop()
        if( l<p ):
            q=partition(A,l,p)
            stack.append((l,q-1))
            stack.append((q+1,p))

A=[124,25,3257,124698,143,6413,1469]
quicksort(A)
print(A)

#qs([x for x in T if x < pivot])++[pivot]++qs(x for x in T if x > pivot)