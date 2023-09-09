# Opis algorytmu:
# Na początku wyznaczam na każdym polu [0][0:m-1] ile ropy jesteśmy 
# w stanie wydobyć z jednej plamy.
# Następnie zachłannie przechodzę przez kolejne pola.
# Wykorzystuję kolejkę, aby wyciągać z niej największe plamy ropy 
# jakie chwilowo mamy w zasięgu w celu zwiększenia zasięgu.
# Jeżeli zabraknie nam paliwa, to wyciągamy z kolejki następną, 
# największą plamę ropy.
# 
# Złożoność:
# O(n*m)

#plamyy ropy
from zad3testy import runtests
from queue import PriorityQueue

def plan(T):
    # zliczanie plamy ropy
    def zloze(T, n, m, row, col):
        if(row >= 0 and row <= n-1 and col >= 0 and col <= m-1\
            and T[row][col] != 0):
            res = T[row][col]
            T[row][col] = 0
            res += (zloze(T, n, m, row+1, col)\
                + zloze(T, n, m, row-1, col)\
                + zloze(T, n, m, row, col+1)\
                + zloze(T, n, m, row, col-1))
            return res
        return 0

    # główna funkcja
    Q, N, M, POS, RESULT = PriorityQueue(), len(T), len(T[0]), 1, 1
    STOPS = []
    STOPS.append(0)

    for i in range(M): T[0][i] = zloze(T, N, M, 0, i)

    zasieg = T[0][0]
    if zasieg >= M-1: return [0]
    if zasieg == 0:   return None

    while zasieg < M-1:
        while POS <= zasieg and POS <= M-1:
            if(T[0][POS] != 0): Q.put((-T[0][POS], POS))
            POS +=1

        ZAS, P = Q.get()
        zasieg -= ZAS
        RESULT +=1
        STOPS.append(P)

    STOPS.sort()
    return STOPS


runtests(plan)
