from egz1atesty import runtests

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    S.sort()
    j=0
    suma=0

    while(S[j]-j>0):
        suma += (S[j]-j)
        j+=1

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
