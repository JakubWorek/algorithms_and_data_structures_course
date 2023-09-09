from egzP9atesty import runtests

def UPDATE(T, index, value):
    global max_index
    while index <= max_index:
        T.set(index, T.get(index)+value)
        index += (index & (-index))

def GETSUM(T, index):
    output = 0
    while index:
        output += T.get(index)
        index -= (index & (-index))
    return output

def ASD(T, p, Q, n):
    #Tutaj proszę wpisać własną implementację
    global max_index
    max_index = n
    output = 0

    for el in Q:
        if el[0] == 0:
            UPDATE(T,el[1]+1,el[2])
        else:
            output += GETSUM(T,el[2]+1) - GETSUM(T,el[1])

    return output


#Podpowiedź. Format zadania jest dość nietypowy (także ze względu na sposób działania testów),
#w takiej formie żadne zadanie raczej nie powinno się pojawić na egzaminie. Zadanie ma na celu
#sprawdzenie zrozumienia struktury #### Drzewa Przedziałowego ####

runtests(ASD, all_tests = True)

