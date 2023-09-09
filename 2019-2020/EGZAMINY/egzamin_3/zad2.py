from zad2testy import runtests

# O(n^2)
def canFall(A, B):
	return B[0] <= A[0] and A[1] <= B[1]

def tower(A):
	n = len(A)
	heights = [1]*n

	for i in range(1, n):
		for j in range(i):
			if canFall(A[i], A[j]):
				heights[i] = max(heights[i],heights[j]+1)

	return max(heights)

# O(nlogn)
def binarySearch(arr, val, fn):
	left = 0
	right = len(arr) -1

	while left <= right:
		mid = (left + right) // 2
		if fn(val, arr[mid]): left = mid + 1
		else: right = mid -1

	return left

def longestSeq(arr, fn = lambda a, b: a>b):
	if len(arr) < 2: return len(arr)

	n = len(arr)
	res = []

	for i in range(n):
		j = binarySearch(res, arr[i], fn)
		if j == len(res): res.append(arr[i])
		else: res[j] = arr[i]

	return res

def tower_nlogn(A):
	n = len(A)
	A = longestSeq(A, lambda curr, prev: curr[0] >= prev[0])
	A = longestSeq(A, lambda curr, prev: curr[1] <= prev[1])
	return len(A)


runtests( tower_nlogn )
