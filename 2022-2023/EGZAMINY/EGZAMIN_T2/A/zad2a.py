# Jakub Worek 414492
#
# wyliczam maksymalny x i y
# tablica GRTTY[i] to liczba punktów których y>=i
# tablica SMLRTX[i] to liczba punktów których x<=i
# tablica EQLTOX[i] to liczba punktów których x==i
# wyliczam je liniowo
# trzeba zauwazyc zaleznosci miedzy tymi wartosciami
# siłą punktu (x, y) jest wartość SMLRTX[x]-GRTTY[y]+EQLTX[x]+1
#
# zlozonosc: O(n) gdzie n to liczba punktów

from egz2atesty import runtests

def dominance(P):
    max_x = max(P, key=lambda p: p[0])[0]
    max_y = max(P, key=lambda p: p[1])[1]

    GRTTY = [0] * (max_y + 1)
    SMLRTX = [0] * (max_x + 1)
    EQLTX = [0] * (max_x + 1)

    for x, y in P:
        GRTTY[y] += 1
        SMLRTX[x] += 1
        EQLTX[x] += 1

    for x in range(1, max_x+1): SMLRTX[x] += SMLRTX[x-1]
    for y in range(max_y-1,-1,-1): GRTTY[y] += GRTTY[y+1]

    max_strength = []
    for x, y in P:
        max_strength.append(SMLRTX[x] - GRTTY[y] - EQLTX[x] + 1)
    return max(max_strength)

runtests( dominance, all_tests = False )