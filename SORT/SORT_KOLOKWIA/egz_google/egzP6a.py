from egzP6atesty import runtests 

'''
    dzielimy nasze hasła na buckety po długościach
    bucket w którym znajduje się najsłabsze dopuszczalne hasło
    to ten, w któym znajduje się hasło oddalone o s najdłuższego hasła
    znajdujemy go sumując długości bucketów (od najdłuższego) aż przekroczymy,
    bądź zrównamy się z s
    w znalezionym buckecie zliczamy litery w hasłach
    następnie szukamy quickselectem naszego hasła
'''

def partition(A,start,end):
    pivot = end
    i = start-1
    for j in range(start,end):
        if A[j][2] >= A[pivot][2]:
            i+=1
            A[i],A[j]=A[j],A[i]
    i+=1
    A[i],A[pivot]=A[pivot],A[i]
    return i

def quickselect(A,start,end,pos):
    if start == end: return

    q=partition(A,start,end)

    if q == pos: return

    if q<pos:
        return quickselect(A,q+1,end,pos)
    else:
        return quickselect(A,start,q-1,pos)

def google ( H, s ):
    
    # dzielimy hasła po długościach na buckety
    maxLen = 0
    for el in H:
        maxLen = max(maxLen,len(el))

    buckets = [[] for _ in range(maxLen+1)]
    for el in H:
        buckets[len(el)].append(el)

    # szukamy indeksu bucketa, w którym znajduje się szukane hasło
    szukaneId = 0
    suma = 0

    for i in range(maxLen, -1, -1):
        suma += len(buckets[i])
        if s <= suma:
            szukaneId = i
            break
    
    # hasłom w buckecie dodajemy ich długość oraz ilość różnych znaków
    T = buckets[szukaneId]
    for i in range(len(T)):
        letters = 0
        for char in T[i]:
            if ord(char) >= 97 and ord(char) <= 122:
                letters +=1
        T[i] = (T[i], len(T[i]), letters)

    # sortujemy w poszukiwaniu naszego hasła
    startId = 0
    endId = len(T)-1
    szukanyId = s - (suma - len(T)) -1 # -1, bo indeksy od 0

    quickselect(T, startId, endId, szukanyId)

    return T[szukanyId][0]


runtests ( google, all_tests=True )