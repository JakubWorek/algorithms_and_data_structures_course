from random import randint

#Quicksort zaimplementowany na podstawie "Wprowadzenia do algorytmów"
#Pesymistycznie: O(n^2)
#Oczekiwana: O(nlogn)

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

def main():
    tab=[]

    for i in range(10):
        num=randint(1,100)
        tab.append(num)

    print(tab)
    quicksort(tab,0,len(tab)-1)
    print(tab)

if __name__ == "__main__": main()