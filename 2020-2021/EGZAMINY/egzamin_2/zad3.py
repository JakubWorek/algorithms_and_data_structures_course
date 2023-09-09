from zad3testy import runtests
from math import inf

def lamps( n,T ):
    """tu prosze wpisac wlasna implementacje"""
    colors = [0]*n
    _max = -inf

    for interval in T:
        for i in range(interval[0], interval[1]+1):
            colors[i] +=1

        cnt = 0
        for i in range(n):
            if colors[i] % 3 == 2: cnt += 1

        _max = max(_max, cnt)

    return _max

    
runtests( lamps )