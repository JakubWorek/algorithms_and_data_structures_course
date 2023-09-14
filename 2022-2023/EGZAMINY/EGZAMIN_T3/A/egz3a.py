# Jakub Worek
# 
# Opis: robię dijkstrę ze zliczaniem ile czasu spędziłem 
# w podróży. Jeżeli przekroczy 16 godzin odpoczywam i dodaję 
# do dystansu czas odpoczynku. 
#
# Złożoność: O(n^2)

from egz3atesty import runtests
from queue import PriorityQueue
from math import inf

def goodknight( G, s, t ):
	n = len(G)
	dist = [[inf]*(16+1) for _ in range(n)]
	Q = PriorityQueue()
	dist[s][0] = 0
	Q.put((dist[s][0], s, 0))

	while not Q.empty():
		curr_dist, u, hours = Q.get()
		for v in range(n):
			if G[u][v] != -1:
				new_hours = hours + G[u][v]
				if new_hours > 16: Q.put((curr_dist+8, u, 0))
				else:
					if dist[v][hours + G[u][v]] > curr_dist + G[u][v]:
						dist[v][hours + G[u][v]] = curr_dist + G[u][v]
						Q.put((dist[v][hours + G[u][v]], v, hours + G[u][v]))

	return min(dist[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
