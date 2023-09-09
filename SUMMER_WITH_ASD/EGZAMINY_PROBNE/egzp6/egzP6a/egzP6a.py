from egzP6atesty import runtests 

# Złożoność O(nk)

def partition(T, p, r):
    pivot = r
    i = p-1
    for j in range(p, r):
        if T[j][2] >= T[pivot][2]:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quickselect(T, p, r, x):
    if p == r:
        return
    q = partition(T, p, r)
    if x == q:
        return
    
    if x < q:
        return quickselect(T, p, q-1, x)
    else:
        return quickselect(T, q+1, r, x)

def google ( H, s ):
    # rozdzielam elementy na buckety po długości
    maxlen = 0
    for el in H: maxlen = max(maxlen, len(el))
    buckets = [[] for _ in range(maxlen+1)]
    for el in H: buckets[len(el)].append(el)

    # wyznaczam bucket w którym znajduje się szukany element
    summ = 0
    id = 0
    for i in range(maxlen, -1, -1):
        summ += len(buckets[i])
        if s <= summ: id = i; break
    
    # w wyznaczonym bucketcie znajduję ilości liter
    T = buckets[id]
    for i in range(len(T)):
        letters = 0
        for letter in T[i]:
            if ord(letter) >= 97 and ord(letter) <= 122: letters += 1
        T[i] = (T[i], len(T[i]), letters)

    # wyznaczam szukane hasło quickselectem
    start = 0
    end = len(T) - 1
    search = s - (summ - len(T)) - 1

    quickselect(T, start, end, search)

    return T[search][0]


runtests ( google, all_tests=False )