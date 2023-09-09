from zad3testy import runtests


def kintersect( A, k ):
	n = len(A)
	longest = 0
	res_spans = []

	if k == 1:
		for i in range(n):
			if A[i][1] - A[i][0] > longest:
				longest = A[i][1] - A[i][0]
				res_spans = [i]
	else:
		for i in range(n):
			A[i] = A[i], i
		A.sort(key=lambda tup: tup[0][1], reverse=True)

		for i in range(n):
			spans = [A[i][1]]
			for j in range(n):
				if i == j or A[j][0][0] > A[i][0][0]: continue
				spans.append(A[j][1])
				if len(spans) == k: break

			if len(spans) < k: continue

			length = min(A[i][0][1], A[j][0][1]) - A[i][0][0]
			if length > longest:
				longest = length
				res_spans = spans

	return res_spans

runtests( kintersect )