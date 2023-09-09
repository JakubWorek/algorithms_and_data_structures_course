from zad1testy import runtests
from functools import cache


def intuse( I, x, y ):
    n = len( I )
    for i in range(n):
        I[i] = (I[i][0], I[i][1], i)
    I.sort()

    sol = []
    F = [False]*n

    @cache
    def rec(idx, y):
        point = I[idx][1]
        if F[idx]: return True
        if point == y: return True

        flag = False
        for i in range(idx+1, n):
            if I[i][0] == point:
                if rec(i, y):
                    F[i] = True
                    sol.append(I[i][2])
                    flag = True
        
        return flag

    for i in range(n):
        if I[i][0] == x:
            if rec(i,y):
                sol.append(I[i][2])

    return list(set(sol))

    
runtests( intuse )


