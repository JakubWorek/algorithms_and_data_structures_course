from random import randint

def heapify(A, n, i):
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


def heapSort(A):
    n=len(A)

    buildHeap(A)

    for i in range(n-1,0,-1):
        A[i],A[0] = A[0],A[i]
        heapify(A, i, 0)


def main():
    tab=[]

    for i in range(10):
        num=randint(1,100)
        tab.append(num)

    print(tab)
    heapSort(tab)
    print(tab)

if __name__ == "__main__": main()