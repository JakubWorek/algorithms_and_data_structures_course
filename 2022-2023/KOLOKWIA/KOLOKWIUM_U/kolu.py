from kolutesty import runtests

def ice_cream( T ):
    # tu prosze wpisac wlasna implementacje
    T.sort(reverse=True)
    n = len(T)
    sol = 0
    mins = 0

    for i in range(n):
        if T[i] - mins > 0:
            sol += T[i] - mins
            mins += 1
        else: break
    return sol

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
