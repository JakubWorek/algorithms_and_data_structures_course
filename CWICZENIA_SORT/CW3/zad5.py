def insert(A,val):
    A.append(val)
    i=len(A)-1
    while i>0:
        if(A[i]>A[(i-1) // 2]):
            A[i],A[(i-1) // 2]=A[(i-1) // 2],A[i]
        i=(i-1)//2
