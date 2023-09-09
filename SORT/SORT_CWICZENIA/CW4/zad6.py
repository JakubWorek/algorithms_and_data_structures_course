#dwa indeksy idące od początku tablicy

def find_colors(T, k):
    A = [0] * k
    zeros = k
    indexes = []
    i = j = A[0]
    while j != len(T) + 1:
        if j == len(T):
            if zeros == 0:
                indexes.append((i, j - 1))
            break
        elif zeros != 0:
            if A[T[j]] == 0:
                zeros -= 1
            A[T[j]] += 1
            j += 1
        else:
            indexes.append((i, j - 1))
            A[T[i]] -= 1
            if A[T[i]] == 0:
                zeros += 1
            i += 1
    return indexes

k = 4
T = [0, 1, 1, 2, 3, 2, 0, 3, 0, 1, 2]
print(find_colors(T, k))