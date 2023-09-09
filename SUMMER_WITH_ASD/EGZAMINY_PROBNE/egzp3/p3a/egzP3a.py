from egzP3atesty import runtests
from math import inf

class Node:
	def __init__(self, wyborcy, koszt, fundusze):
		self.next = None
		self.wyborcy = wyborcy 
		self.koszt = koszt 
		self.fundusze = fundusze 
		self.x = None

def knapsack(DP, S, P, W, i):
    if S < 0:
        return -inf
    if i >= len(P):
        return 0
    if DP[i][S] != None:
        return DP[i][S]
    d1 = knapsack(DP, S-W[i], P, W, i+1) + P[i]
    d2 = knapsack(DP, S, P, W, i+1)
    DP[i][S] = max(d1, d2)
    return DP[i][S]

# problemy plecakowe
def wybory(T):
    res = 0

    for el in T:
        S = el.fundusze
        P = []
        W = []
        pp = el
        while pp != None:
            P.append(pp.wyborcy)
            W.append(pp.koszt)
            pp = pp.next
        DP = [[None for _ in range(S+1)] for __ in range(len(P))]
        res += knapsack(DP, S, P, W, 0)

    return res

runtests(wybory, all_tests = True)