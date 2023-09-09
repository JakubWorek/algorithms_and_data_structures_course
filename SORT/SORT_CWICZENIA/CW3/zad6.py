# Scalanie k posortowanych list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def heapify(A, n, i): #TO DO: naprawic heapify, żeby od najmniejszej dawał
    max_ind = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[max_ind]:
        max_ind=l

    if r < n and A[r] > A[max_ind]:
        max_ind=r

    if max_ind != i:
        A[i],A[max_ind] = A[max_ind],A[i]
        heapify(A,n,max_ind)

def buildHeap(A):
    n=len(A)
    for i in range( n // 2 - 1 , -1, -1):
        heapify(A, n, i)

def merge(S):
    buildHeap(S)
    wartownik=Node(None)
    curr=wartownik

    while(S):
        curr.next=S[0]
        S[0]=S[0].next
        curr=curr.next
        #curr.next=None
        S[0],S[-1]=S[-1],S[0]
        if(S[-1] is None): S.pop()
        heapify(S,len(S)-1,0)
    
    return wartownik.next
