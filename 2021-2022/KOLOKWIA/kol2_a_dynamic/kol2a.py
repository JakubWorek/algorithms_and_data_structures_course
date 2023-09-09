from kol2atesty import runtests
from math import inf

JACEK = 0
MARIAN = 1
CONTROL_POINT = False

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje
    n = len( P )
    DP = [[None, None] for _ in range(n) ]

    for i in range(n):
        P[i] = (P[i][0], P[i][1], i)
    P.sort(key=lambda x: x[0])

    fill(P,B,DP,0,JACEK)
    return get_res(P,B,DP)

def fill(P,B,DP,point,driver):
    if DP[point][driver] is not None: return DP[point][driver]

    n = len(P)
    cnt_ctrl = 0
    cnt_chng = 0
    DP[point][driver] = inf

    for i in range(point + 1, n):
        if i == n-1 or P[i][0] == B:
            if driver == MARIAN:
                if P[i][1] == CONTROL_POINT: cnt_ctrl += 1
                DP[point][driver] = min(DP[point][driver], cnt_ctrl)
            else:
                DP[point][driver] = 0
            break

        if P[i][1] == CONTROL_POINT: cnt_ctrl += 1
        else:
            cnt_chng += 1
            if driver == JACEK:
                DP[point][JACEK] = min(DP[point][JACEK], fill(P,B,DP, i, MARIAN))
            else:
                DP[point][MARIAN] = min(DP[point][MARIAN], fill(P,B,DP, i, JACEK) + cnt_ctrl)
            if cnt_chng == 3: break
    
    return DP[point][driver]

def get_res(P,B,DP):
    n = len(P)
    driver = JACEK
    point = 0
    i = 1
    cnt_ctrl = 0
    res = []

    while i < n and P[i][0] < B:
        if P[i][1] == CONTROL_POINT: cnt_ctrl += 1
        else:
            if driver == JACEK and DP[point][JACEK] == DP[i][MARIAN]:
                res.append(P[i][2])
                point = i
                cnt_ctrl = 0
                driver = MARIAN
            elif driver == MARIAN and DP[point][MARIAN] == DP[i][JACEK] + cnt_ctrl:
                res.append(P[i][2])
                point = i
                cnt_ctrl = 0
                driver = JACEK
        i+=1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )