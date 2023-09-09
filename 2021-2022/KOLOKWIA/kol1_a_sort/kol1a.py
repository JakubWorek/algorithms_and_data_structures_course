# Wiadro sort, działanie w komentarzach

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
