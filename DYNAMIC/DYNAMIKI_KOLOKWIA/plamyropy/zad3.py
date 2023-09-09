# plamy ropy
from zad3testy import runtests
from queue import PriorityQueue

def zloze(T, n, m, c_row, c_col):
    if(c_row >= 0 and c_row <= n-1 and c_col >= 0 and c_col <= m-1\
        and T[c_row][c_col] > 0):
        res = T[c_row][c_col]
        T[c_row][c_col] = 0
        return res + zloze(T, n, m, c_row+1, c_col)\
            + zloze(T, n, m, c_row-1, c_col)\
            + zloze(T, n, m, c_row, c_col+1)\
            + zloze(T, n, m, c_row, c_col-1)
    else: return 0


def plan(T):
    n = len(T)
    m = len(T[0])
    R = [0]*m
    res = [0]

    for i in range(m):
        R[i] = zloze(T, n, m, 0, i)

    zasieg = R[0]
    if zasieg >= m-1: return res

    wskaznik = 1
    Q = PriorityQueue()

    while wskaznik != m-1:
        while wskaznik <= zasieg and wskaznik != m-1:
            if(R[wskaznik] != 0): Q.put((-R[wskaznik], wskaznik))
            wskaznik +=1

        Z, ind = Q.get()
        Z *= -1
        res.append(ind)
        zasieg += Z
        if zasieg >= m-1:
            res.sort()
            return res
    
    return None



runtests(plan)