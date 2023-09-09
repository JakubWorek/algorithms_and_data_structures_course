# Jakub Worek 414492
# 
# f(i, j) = minimalna suma odległości biurowców z pozycji X[0] do X[i]
# do przydzielonych im działek, przy założeniu że biurowiec 
# z pozycji X[i] ma przydzieloną działkę z pozycji Y [j].
#
# f(1, j) - bierzemy pod uwagę wszystkie parkingi i wybieramy najbliższy
# 
# f(i, j) = min(f(i-1, k-1) + |X[i-1] - Y[j-1]|) dla k = j, j-1, ..., 1
#
# O(nm^2)

from egz2btesty import runtests

def parking(X,Y):
    n = len(X)
    m = len(Y)

    # Tworzymy tablicę dp, gdzie dp[i][j] będzie przechowywać minimalną sumę odległości
    # dla i biurowców i j działek na parkingi.
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(j, 0, -1):
                # Aktualizacja dp[i][j] poprzez porównanie z dp[i-1][k-1] + odległość.
                dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + abs(X[i - 1] - Y[j - 1]))

    # Minimalna suma odległości będzie znajdować się w ostatnim wierszu.
    min_distance = min(dp[n])

    return min_distance

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True)