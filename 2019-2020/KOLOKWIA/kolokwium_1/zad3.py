'''
Najpierw sortujemy tablicę. Kolejnym krokiem jest przejście 
liniowe po posortowanej tablicy i sprawdzanie również w sposób 
liniowy, czy dana liczba jest sumą dwóch innych wartości z tablicy. 
Oczywiście możemy pomijać już liczby, dla których wcześniej to 
sprawdziliśmy, ponieważ wiemy, że istnieje dla nich już suma. 
Ponieważ poszukiwanie sumy robimy dla n liczb w czasie O(n) dla 
każdej, sumaryczna złożoność czasowa algorytmu wyniesie O(n^2)
'''

from zad3tests import runtests

def is_sum_of_two(A, idx):
    l = 0
    r = len(A) - 1

    while l < r:
        if l == idx: l+=1; continue
        if r == idx: r-=1; continue

        if A[l] + A[r] > A[idx]: r -=1
        elif A[l] + A[r] < A[idx]: l +=1
        else: return True

    return False

def check_sums(A):
    n = len(A)
    if n < 3: return False
    A.sort()

    if not is_sum_of_two(A,0): return False

    for i in range(1,n):
        if A[i] != A[i-1] and not is_sum_of_two(A,i): return False

    return True

runtests(check_sums)