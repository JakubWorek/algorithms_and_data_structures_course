from kol1btesty import runtests

def strToList(str):
    lista=[0 for _ in range(26)]

    for char in str:
        lista[ord(char)-97] +=1
    
    return lista

def counting_sort(T, ind, maxLicz):
    n=len(T)
    C = [0]*(maxLicz+1)
    B = [0]*len(T)

    for i in range(n):
        C[(T[i][ind])] = C[(T[i][ind])] +1

    for i in range(1, maxLicz):
        C[i] += C[i-1]
    
    for i in range(n-1,-1,-1):
        B[C[(T[i][ind])]-1]=T[i]
        C[T[i][ind]] -=1

    for i in range(n):
        T[i] = B[i]


def radix_sort(T):
    maxLicznoscChar=0
    for i in range(26):
        for j in range(len(T)):
            if T[j][i] > maxLicznoscChar:
                maxLicznoscChar = T[j][i]

    for i in range(25,-1,-1):
        counting_sort(T,i,maxLicznoscChar+1)



def f(T):
    n=len(T)

    for i in range(n):
        T[i]=strToList(T[i])

    radix_sort(T)

    max_ana=1
    ana=1
    for i in range(1,n):
        if(T[i] == T[i-1]):
            ana+=1
        else:
            max_ana=max(max_ana,ana)
            ana=1
    
    max_ana=max(max_ana,ana)

    return max_ana


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
