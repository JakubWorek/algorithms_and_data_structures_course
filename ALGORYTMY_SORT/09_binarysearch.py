def recursive_binary_search(T, l, r, x):
    if r >= l:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            return recursive_binary_search(T, l, mid - 1, x)
        elif T[mid] < x:
            return recursive_binary_search(T, mid + 1, r, x)
    else:
        return -1


def iterative_binary_search(T, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1