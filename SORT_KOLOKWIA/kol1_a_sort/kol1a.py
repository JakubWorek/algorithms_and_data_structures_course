'''
Mówimy, że dwa napisy są sobie równoważne, jeśli albo są 
identyczne, albo byłyby, gdyby jeden z nich zapisać od tyłu. 
Dana jest tablica T zawierająca n napisów o łącznej długości 
N ( N>=n; napisy składają się wyłącznie z małych liter alfabetu 
łacińskiego) Siłą napisu T[i] jest liczba indeksów j takich że 
napisy T[i] oraz T[j] są sobie równoważne. Napis T[i] jest 
najsilniejszy, jeśli żaden inny napis nie ma większej siły. 
Proszę zaimplementować w pythonie funkcję g(T), która zwraca 
siłę najsilniejszego napisu z tablicy T. Algorytm powinien 
być możliwie najszybszy.
'''

# bucketsort 

from kol1atesty import runtests

def g(T):
    n=len(T)
    
    #dzielimy wiadro-sortem na wiadra o tej samej długości słowa
    max_len=0
    for i in range(n):
        max_len=max(max_len,len(T[i]))

    buckets = [[] for _ in range(max_len+1)]
    for slowo in T:
        buckets[len(slowo)].append(slowo)
    
    max_strength=0
    for bucket in buckets:
        if(len(bucket) != 0):
            #budujemy coś na kształt słownika i zliczamy maxymalne powtórzenia
            keys = []
            values = []
            for s in bucket:
                r = s[::-1]
                if s == r:
                    if s not in keys:
                        keys.append(s)
                        values.append(0)
                    values[keys.index(s)] +=1
                else:
                    if(s<r):
                        if s not in keys:
                            keys.append(s)
                            values.append(0)
                        values[keys.index(s)] +=1
                    else:
                        if r not in keys:
                            keys.append(r)
                            values.append(0)
                        values[keys.index(r)] +=1
            max_strength = max(max_strength,max(values))
            
    return max_strength

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
