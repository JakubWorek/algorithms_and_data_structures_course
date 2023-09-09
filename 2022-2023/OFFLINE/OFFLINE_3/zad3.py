# Jakub Worek 20.03.2023-26.03.2023                                                     #
#                                                                                       #
# Dowód poprawności:                                                                    #
# Dzielimy słowa z tablicy na wiadra ze słowami o tej samej długości.                   #
# Budujemy słownik ze słów i ich odwrotności zliczający powtórzenia w wiadrze.          #
# Zwracamy maksymalną ilość powtórzeń.                                                  #
#                                                                                       #
# Złożoność:                                                                            #
# O(n+n^2) // byłoby O(n), gdyby użyć słownika                                          #
#                                                                                       #
#########################################################################################


from zad3testy import runtests

def strong_string(T):
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


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
