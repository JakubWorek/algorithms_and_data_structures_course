from egz2btesty import runtests

def magic( C ):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        for j in range(1, 4):
            obecna_komnata = i
            ile_w_skrzyni = C[i][0]
            nowa_komnata = C[i][j][1]
            ile_ma_byc_w_skrzyni = C[i][j][0]

            if nowa_komnata > obecna_komnata and\
                dp[obecna_komnata] != -1 and\
                ile_w_skrzyni - ile_ma_byc_w_skrzyni <= 10:
                dp[nowa_komnata] = max(dp[nowa_komnata],\
                                        dp[obecna_komnata] +ile_w_skrzyni - ile_ma_byc_w_skrzyni)

    return dp[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = False )
