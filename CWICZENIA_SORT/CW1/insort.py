from random import randint

#Quicksort zaimplementowany na podstawie "Wprowadzenia do algorytmów"
#O(n^2)

def insertionsort(A):
    for j in range(1,len(A)):
        key = A[j]
        #wstawiamy key do posortowanej poczatkowej czesci tablicy
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key

def main():
    tab=[]

    for i in range(10):
        num=randint(1,100)
        tab.append(num)

    print(tab)
    insertionsort(tab)
    print(tab)

if __name__ == "__main__": main()