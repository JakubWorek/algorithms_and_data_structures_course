from zad2testy import runtests

def depth1(L): # O(n^2)
    L.sort(key=lambda x: x[0])
    max_ = 0
    n = len(L)
    for i in range(n):
        curr = 0
        for j in range(i+1, n):
            if L[i][0] <= L[j][0] and L[i][1] >= L[j][1]:
                curr += 1
        max_ = max(max_, curr)
    
    return max_


# 1) sortujemy tablice przedzialow rosnaco wzgledem poczatku przedzialu
# 2) szukamy  kandydatow na posiadanie najwiecej przedzialow wewnatrz
#   swojego przedzialu
#   przedzialy zawarte w rozpatrywanym przedziale sa pomijane
#   pomijanie nastepuje rowniez w przypadku tego samego poczatku 
#   (dlatego sortowalismy wczesniej)
#   odnalezienie 1. przedzialu niezawierajacego sie w rozaptrywanym 
#   przedziale  skutkuje jego przeniesieniem na stos 
#   kolejny rozpatrywany przedzial to ten, co dopiero wrzucilismy na
#   stos
# 3) wydobywamy ze stosu kolejne przedzialy, sprawdzamy czy "pod nim"
#    czasem nie wystepuja inne z tym samym poczatkiem, a nastepnie 
#    szukamy zawierajacych sie w rozpatrywanym


def depth(L): # O(nlogn)
    L.sort(key=lambda x: x[0])
    S = [0]
    n = len(L)

    curr = 0
    for i in range(1,n):
        if L[i][1] > L[curr][1] and L[i][0] != L[curr][0]:
            S.append(i)
            curr = i

    max_ = 0
    for i in S:
        curr = 0
        start = L[i][0]
        end = L[i][1]
        tmp = i-1

        while tmp >= 0 and start == L[tmp][0]:
            curr +=1
            tmp -=1

        for j in range(i+1, n):
            if L[j][1] <= end: curr += 1
            elif L[j][0] == start:
                end = L[j][1]
                curr += 1
            elif end < L[j][0]: break

        max_ = max(max_, curr)
        if n-i-1-max_ <= 0: return max_
    
    return max_



runtests( depth ) 
