from zad3testy import runtests

def insertion_sort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T


def bucket_sort(T):
    bucket = [[] for _ in range(len(T))]
    for i in T:
        index = int(i)
        bucket[index].append(i)
    for i in range(len(T)):
        bucket[i] = insertion_sort(bucket[i])
    k = 0
    for i in range(len(T)):
        for j in range(len(bucket[i])):
            T[k] = bucket[i][j]
            k += 1
    return T

def SortTab(T,P):
    # tu prosze wpisac wlasna implementacje
    return bucket_sort(T)

runtests( SortTab )