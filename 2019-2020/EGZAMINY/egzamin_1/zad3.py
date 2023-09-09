from zad3testy import runtests
from math import log

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

def bucket_sort(arr, k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int(elem // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1

def fast_sort(tab,a):
    n = len(tab)
    res = [0 for _ in range(n)]
    for i in range(n):
        res[i] = log(tab[i], a)
    bucket_sort(res, 1)
    for i in range(n):
        res[i] = a**res[i]
    return res


runtests( fast_sort )
