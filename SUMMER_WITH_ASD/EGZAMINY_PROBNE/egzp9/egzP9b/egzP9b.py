from egzP9btesty import runtests

# Tworzę właściwy graf i puszczam DFS-a opartego o stos.

def dyrektor( G, R ):
	def find_eulerian_cycle(graph, start_vertex):
		stack = [start_vertex]
		eulerian_cycle = []

		while stack:
			current_vertex = stack[-1]

			if graph[current_vertex]:
				next_vertex = graph[current_vertex].pop()
				stack.append(next_vertex)
			else:
				eulerian_cycle.append(stack.pop())

		return eulerian_cycle[::-1]
	
	graph = {}
	for i in range(len(G)):
		for u in G[i]:
			if i not in graph: graph[i] = []
			graph[i].append(u)

	for i in range(len(R)):
		for u in R[i]:
			if i in graph and u in graph[i]:
				graph[i].remove(u)

	start_vertex = 0
	eulerian_cycle = find_eulerian_cycle(graph, start_vertex)
	return eulerian_cycle
	
runtests(dyrektor, all_tests=True)
