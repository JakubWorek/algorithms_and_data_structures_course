from egz3btesty import runtests

def maze( L ):
    n = len( L )
    DPG = [[-1 for _ in range( n )] for __ in range( n )] # w górę
    DPD = [[-1 for _ in range( n )] for __ in range( n )] # w dół

    if( L[0][0] == '#' or L[n-1][n-1] == '#' ): return -1

    DPG[0][0], DPD[0][0] = 0,0

    for row in range(1,n):
        if L[row][0] == '#': break
        DPD[row][0] = DPD[row-1][0]+1

    for col in range( 1,n ):
        for row in range(n):
            if L[row][col] == '#': continue
            if DPG[row][col-1] == -1 and DPD[row][col-1] == -1: continue
            val = max(DPG[row][col-1], DPD[row][col-1]) + 1
            DPG[row][col] = val
            DPD[row][col] = val
        for row in range(n):
            if L[row][col] == '#': continue
            if DPG[row][col-1] == -1 and DPD[row][col-1] == -1 : continue
            row1, row2 = row-1,row+1
            while row1 >=0:
                if L[row1][col] == '#': break
                DPG[row1][col] = max(DPG[row1][col], DPG[row1+1][col]+1)
                row1 -=1
            while row2 <n:
                if L[row2][col] == '#': break
                DPD[row2][col] = max(DPD[row2][col], DPD[row2-1][col]+1)
                row2 +=1
        
    if DPG[n-1][n-1] == -1 and DPD[n-1][n-1] == -1: return -1
    return max(DPG[n-1][n-1], DPD[n-1][n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
