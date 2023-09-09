from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    Q = PriorityQueue()
    N = len(T)
    POS = 1
    RESULT = [0]

    zasieg = T[0]
    if zasieg >= N-1: return RESULT
    if zasieg == 0:   return None

    while zasieg < N-1:
        while POS <= zasieg and POS <= N-1:
            if(T[POS] != 0): Q.put((-T[POS],POS))
            POS +=1

        zkolejki = Q.get()
        zasieg -= zkolejki[0]
        postoj = zkolejki[1]
        RESULT.append(postoj)

    return sorted(RESULT)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = False )