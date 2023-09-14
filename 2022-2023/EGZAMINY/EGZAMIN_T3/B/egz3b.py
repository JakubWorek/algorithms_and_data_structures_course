# Jakub Worek
#
# Opis: tzw bruteforce, sprawdzam wszystkie przedziały
# 
# Złożoność: O(n^2)

from egz3btesty import runtests

def areDisjoint(interval1, interval2):
	if interval1[0] > interval2[1] or interval1[1] < interval2[0]: 
		return True
	return False

def areContaining(interval1, interval2):
	if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]: 
		return True
	if interval2[0] <= interval1[0] and interval2[1] >= interval1[1]:
		return True
	return False

def uncool( P ):
	# tu prosze wpisac wlasna implementacje
	n = len(P)
	for i in range(n): P[i] = (P[i][0], P[i][1], i)
	P.sort(key = lambda x: x[0])
	
	for i in range(n-1):
		for j in range(i+1, n):
			if areDisjoint(P[i], P[j]): continue 
			if areContaining(P[i], P[j]): continue
			return (P[i][2], P[j][2])

	return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
