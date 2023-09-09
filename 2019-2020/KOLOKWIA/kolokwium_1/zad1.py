'''
Ponieważ mamy posortować liczby według tego, która z nich jest 
ładniejsza, konieczne jest najpierw wymyślenie klucza, po którym
będzie odbywało się sortowanie.Od razu na myśl przychodzą algorytmy 
sortowania o złożoności liniowej. Wiemy, że są to liczby naturalne, 
więc z powodzeniem można skorzystać z takiego algorytmu, tylko 
który dokładnie wybrać? Bucket Sort odpada, ponieważ nie wiemy 
nic o rozkładzie liczb. Najlepszy okazuje się Counting Sort, 
ale musimy odpowiednio przygotować te liczby do sortowania, 
a algorytm odpowiednio zmodyfikować.
Można wyciągnąć wniosek, że największe znaczenie ma liczba cyfr 
jednokrotnych, później jest liczba cyfr wielokrotnych. Warto 
więc podzielić liczby tak, by najpierw były sortowane po mniej 
znaczącej wartości (niemalejąco, bo im większa, tym liczba 
brzydsza), a więc po liczbie cyfr wielokrotnych, a następnie 
po bardziej znaczącej liczbie cyfr jednokrotnych (nierosnąco, 
bo im większa, tym liczba ładniejsza). Musimy więc napisać 
funkcję, która zwróci nam obie te wartości, a następnie, aby 
za każdym razem nie zliczać na nowo tych wartości, zapisać 
np. w postaci 3-elementowej krotki tę liczbę, jej liczbę 
cyfr jednokrotnych i liczbę cyfr wielokrotnych.
Możemy wykorzystać taki trick, że każdą z liczb przekształcimy 
na inną liczbę, która będzie zależała od liczby cyfr jednokrotnych 
i liczby cyfr wielokrotnych, zgodnie z poniższym wzorem:
pretty_num = (10 - single_count) * 100 + multiple_count
gdzie 'pretty_num' będzie liczbą, po której będziemy sortować 
liczby z tablicy wejściowej, 'single_count' to liczba pojedynczych 
cyfr, a 'multiple_count' to liczba cyfr wielokrotnych. Wzór ma 
taką postać, ponieważ obie wartości ('single_count' oraz 
'multiple_count') są z przedziału 0,1,...,9,10 , więc aby jedna 
nie nachodziła na drugą, musimy pierwszą z nich (bardziej znaczącą) 
umieścić z przodu liczby wynikowej, a więc przesunąć o 2 miejsca 
w lewo, robiąc miejsce dla pozostałej, maksymalnie 2-cyfrowej 
liczby. Nie używamy po prostu 'single_count', ponieważ chcemy, 
że by najpierw były liczby najładniejsze, czyli te, dla których 
'single_count' ma wartość największą. Ponieważ Counting Sort 
z reguły sotuje liczby w kolejności niemalejącej, musimy 
spowodować, aby liczby najładniejsze, zmapowane do 'pretty_num' 
miały najmniejszą wartość. Oczywiście do liczby dodajemy 
'multiple_count' już normalnie, bo im większa wartość, tym liczba 
jest brzydsza, a więc będzie dalej.
'''

from zad1tests import runtests

def prettify(num):
    counts = [0]*10
    copy = num

    while num:
        num, digit = divmod(num, 10)
        counts[digit] += 1

    single = multi = 0
    for count in counts:
        if count > 1: multi += 1
        elif count == 1: single += 1

    return copy, (10-single)*100 + multi

def countingSort(A, key):
    n = len(A)
    # Allocate memory for required temporary arrays
    counts = [0] * 1011  # Max possible value is 10 * 100 + 10 = 1010 and min is 0
    temp = [None] * n
    # Count values repetitions
    for val in A:
        counts[key(val)] += 1
    # Modify the counts array to indicate how many values are not greater than the current one
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    # Rewrite values to the temp sorted array
    for i in range(n-1, -1, -1):
        idx = key(A[i])
        counts[idx] -= 1
        temp[counts[idx]] = A[i]
    # Rewrite sorted values to the initial array
    for i in range(len(temp)):
        A[i] = temp[i]


def pretty_sort(A):
    n = len(A)
    for i in range(n):
        A[i] = prettify(A[i])

    countingSort(A, lambda x: x[1])

    for i in range(n):
        A[i] = A[i][0]

    return A

runtests(pretty_sort)