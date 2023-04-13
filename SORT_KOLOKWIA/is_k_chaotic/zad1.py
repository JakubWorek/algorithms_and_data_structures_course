from zad1testy import runtests


def chaos_index( T ):
    n = len(T)
    for i in range(n):
        T[i]=(T[i],i)

    k=0
    T.sort()

    for i in range(n):
        k = max(k, abs(T[i][1]-i))

    return k


runtests( chaos_index )
