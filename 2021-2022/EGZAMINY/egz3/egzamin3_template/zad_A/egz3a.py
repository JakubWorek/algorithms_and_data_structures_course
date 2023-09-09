# Podejście zachłanne:
# Wszystkie punkty dodaję do tablicy z rozróżnieniem czy to początek
# czy koniec. Tablicę sortuję. Idąc po tablicy szukam takiego fragmentu
# że punkty będące początkami przedziałów występują obok siebie najliczniej
# Zachłanne podejście jest poprawne, ponieważ ilość punktów rozpoczynających
# przedział występująca obok siebie oznacza, że żaden z przedziałów się
# jeszcze nie zakończył i powstanie zaspa o wysokości równej liczbie tych
# przedziałów. Dopiero natrafienie na zamknięcie przedziału powoduje,
# że ilość śniegu może się zmniejszyć.
#
# Złożoność czasowa: O(nlogn)

from egz3atesty import runtests

def snow( T, I ):
    A = []
    for x,y in I:
        A.append((x,0))
        A.append((y,1))
    A.sort()

    n = len(A)
    sol, cnt = 0, 0
    for i in range(n):
        if A[i][1] == 0: cnt+=1
        else: cnt-=1
        sol = max(sol, cnt)

    return sol

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
