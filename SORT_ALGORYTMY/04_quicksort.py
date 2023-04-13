def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quicksort(T, p, r):
    if len(T) == 1:
        return T
    if p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        quicksort(T, q+1, r)


def iterative_quicksort(T):
    S = []
    p = 0
    r = len(T)-1
    S.append((p, r))
    while len(S) > 0:
        (p, r) = S.pop()
        if p < r:
            q = partition(T, p, r)
            if q-p > r-1:
                S.append((p, q-1))
                S.append((q+1, r))
            else:
                S.append((q+1, r))
                S.append((p, q-1))


def quicksort_one_rec(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q-p <= r-q:
            quicksort_one_rec(T, p, q-1)
            p = q+1
        else:
            quicksort_one_rec(T, q, r)
            r = q-1