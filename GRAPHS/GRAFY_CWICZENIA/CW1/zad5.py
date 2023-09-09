# Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym ujściem, jeśli:
#   (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz
#   (b) nie istnieje żadna krawędź wychodząca z t.
# Proszę podać algorytm znajdujący uniwersalne ujście (jeśli istnieje)
# przy reprezentacji macierzowej grafu.

# w wierszu same 0
# w kolumnie same 1

"""
    1
    1
0 0 0 0 0
    1
    1
"""

# idziemy w lewo aż nie 0
# idziemy w dół aż nie 1

# O(n^2) i O(n)

def uniwersale_ujscie_On2(G):
    result = []
    for i in range(len(G)):
        all_zeros = True
        for j in range(len(G)):
            if G[i][j] == 1:
                all_zeros = False
                break
        if all_zeros:
            result.append(i)
    for u in result:
        all_ones = True
        for v in range(len(G)):
            if u != v and G[v][u] == 0:
                all_ones = False
        if all_ones:
            return u
    return False

def uniwersalne_ujscie_On(G):
    i = j = 0
    while i < len(G) and j < len(G):
        if G[i][j] == 1:
            i += 1
        else:
            j += 1
    i = min(i, j)
    for k in range(len(G)):
        if G[i][k] != 0:
            return False
        if G[k][i] != 1 and k != i:
            return False
    return i