# Szukamy najbliżsego powtórzenia danej liczby w tablicy A
#
# Złożoność: O(nk)

from zad3testy import runtests

def longest_incomplete( A, k ):
    # tu prosze wpisac wlasna implementacje
    n = len(A)
    _max = 0
    C = []

    for i in range(n):
        if A[i] not in C: C+=[A[i]]

    for num in range(k):
        curr = 0
        for i in range(n):
            if A[i] == C[num]: curr = 0
            else: curr += 1

            _max = max(curr, _max)

    return _max

runtests( longest_incomplete ) 
