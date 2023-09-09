from egzP7btesty import runtests 

OVERPICKED = -1
PICKED = 1
NOTPICKED = 0

def ogrod( S, V ):
    n = len( S )
    m = len( V )
    res = 0

    for i in range( n ):
        S[i] -= 1

    for i in range(n):
        isTaken = [NOTPICKED for _ in range(m)]
        output = 0
        for j in range(i, n):
            if isTaken[S[j]] == NOTPICKED:
                output += V[S[j]]
                isTaken[S[j]] = PICKED
            elif isTaken[S[j]] == PICKED:
                res = max(res, output)
                output -= V[S[j]]
                isTaken[S[j]] = OVERPICKED
            elif isTaken[S[j]] == OVERPICKED:
                pass
        res = max(res, output)
    return res
    
runtests(ogrod, all_tests = True)