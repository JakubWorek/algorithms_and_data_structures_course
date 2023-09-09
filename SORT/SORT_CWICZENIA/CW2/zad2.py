def inwersje(A):
    n=len(A)
    cnt=0
    for i in range(n-1):
        for j in range(i,n):
            if A[i]>A[j]: cnt+=1
    return cnt

#def inwersjeMergeSort

# globalny cnt
# robimy mergesorta do momentu podziału na podwójne elementy
# sumujemy to co robi merge jak szuka najmniejszego elementu


print(inwersje([4,3,2,1]))