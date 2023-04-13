from zad3testy import runtests
import math

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        #wstawiamy key do posortowanej poczatkowej czesci tablicy
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key

def fast_sort(tab, a):
    # tu prosze wpisac implementacje
    n = len(tab)

    # znajdujemy wykładniki x = loga(a^x)
    for i in range(n):
        tab[i]= math.log(tab[i],a)

    # robimy bucketsort
    buckets = [[] for _ in range(11)]
    for i in tab:
        index = int(10*i)
        buckets[index].append(i)

    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    ind=0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            tab[ind] = buckets[i][j]
            ind+=1
    
    # odtwarzamy a**x
    for i in range(n):
        tab[i] = a**tab[i]

    return tab

runtests( fast_sort )
