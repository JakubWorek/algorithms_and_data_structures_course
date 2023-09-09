'''
Przechodzimy po tablice, pamiętając ostatni "False" i sprawdzamy za 
każdym razem, czy element na którym jesteśmy, nie będący Falsem, 
wskazuje (jego funkcja haszująca) za False (czyli h(i)>=False_index), 
jak nie, to znalezliśmy szukany False, który nam psuje zabawe. 
Trzeba zwrócić uwagę na to, że możemy wejść w tablicę z drugiej 
strony, w tym przypadku mamy sprawdzić, czy ten False nie jest 
czasem po drodze od hash(el) do danego elementu, robimy to 
w następujący sposób:
        1) curr_last_False może być do przekroczenia tablicy  
    (curr_last_False>=hash i curr_last_False<=curr_i+N), 
    gdzie curr_last_False - Ostatni False, hash - wynik funkcji 
    haszującej dla elementa pod indeksem curr_i, N - rozmiar tablicy
        2) curr_last_False może być po przekroczeniu tablicy 
    (curr_last_False+N>=hash i curr_last_False<=i)
Jak już znaleźliśmy curr_last_False, który by spełniał jeden 
z powyższych warunków, to ustawiamy jego pole taken na True i 
jak bedziemy iterowali (szukali) elementu to po prostu przejdziemy 
przez niego, ew. mozna ustawic key na FLAGA, zeby napewno nie 
bylo tego slowa.
Złożoność algorytmu -> O(n)
'''


class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        
    def __str__(self):
        if not self.taken:
            print('pusty')
        else:
            print('klucz: ', self.key)


def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N


N=11
hash_tab = [Node() for i in range(N)]


def recover(hash_tab):
    curr_last_false = -1
    # W przypadku, gdy pierwsze elementy będą niepuste, 
    # curr_last_false się nie napisze
    for i in range(len(hash_tab)):
        if hash_tab[i].taken == False:
            curr_last_false = i
    i = -1
    for node_i in hash_tab:
        i += 1
        if node_i.taken == False:
            curr_last_false = i
            continue

        hash = h(node_i.key)

        if hash <= i:
            if curr_last_false >= hash and curr_last_false <= i:
                hash_tab[curr_last_false].taken = True
                hash_tab[curr_last_false].key = "FLAGA"

        # mamy or dla dwóch przypadków gdy przeskoczyliśmy N 
        # i wróciliśmy na początek, curr_last_false mógł być 
        # jako przed przeskoczeniem
        else:   
            if (curr_last_false >= hash and \
                curr_last_false <= i + len(hash_tab)) \
                or (curr_last_false + len(hash_tab) >= hash and \
                curr_last_false<= i):
                hash_tab[curr_last_false].taken = True
                hash_tab[curr_last_false].key = "FLAGA"
