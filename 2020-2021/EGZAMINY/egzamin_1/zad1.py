from zad1testy import runtests


def chaos_index( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    T.sort(key = lambda x: x[0])
    k = 0
    for i in range(n):
        k = max(k, abs(T[i][1] - i))
    return k


runtests( chaos_index )
