# 2) koszt przejazdu minimalny (każda stacja ma cene za litr)
# Na każdej stacji możemy tankować ile chcemy

# Zauważmy, że podróż najlepiej podzielić jest na 3 etapy:
#   Początkowy - dotarcie do stacji, na której będziemy po raz 
# pierwszy tankować (nie musi być to koniecznie pierwsza stacja),
#   Przemieszczanie się pomiędzy stacjami paliw (tak najłatwiej jest
# opisać ruch czołgu, ponieważ nas nie obchodzą chwile, w których znajduje się on pomiędzy stacjami, a jedynie to, gdzie się on zatrzymuje, aby zatankować),
#   Zatankowanie ostatni raz i wyruszenie do celu (nie musimy 
# tankować na ostatniej stacji, jaka znajduje się przed punktem 
# docelowym, ostatnie tankowanie może mieć miejsce wcześniej; 
# tankujemy tylko tyle, ile trzeba, aby najlepiej "na pustym baku" 
# dojechać do celu).

def get_first_station(S, P, L):
    min_idx = 0
    for i in range(1, len(S)):
        if S[i] > L: break
        if P[i] < P[min_idx]:
            min_idx = i
    return min_idx


def get_next_station(S, P, L, i, t):
    if i + 1 == len(S) or S[i + 1] - S[i] > L or S[i + 1] >= t:
        return -1
    
    j = min_idx = i + 1
    while j < len(S) and S[j] - S[i] <= L and S[j] < t:
        if P[j] < P[i]:
            return j
        if P[j] < P[min_idx]:
            min_idx = j
        j += 1
    
    if S[i] + L >= t:
        return -1
    
    return min_idx

def tank(L: 'capacity of tank of a tank',
         S: 'array with distances of stations from the starting point',
         P: 'array of fuel prices on appropriate stations',
         t: 'distance to the target point',
         fuel: 'initial amount of fuel'):
    n = len(S)
    if fuel >= t:
        return 0
    if S[0] > fuel or S[n - 1] + L < t:
        return -1

    total_cost = 0
    i = get_first_station(S, P, fuel)
    fuel -= S[i]

    while i >= 0:
        next_i = get_next_station(S, P, L, i, t)
#         print(f"{i} -> {next_i}")

        if next_i > 0:
            distance = S[next_i] - S[i]
            if P[next_i] < P[i]:
                refueled = distance - fuel
            else:
                refueled = L - fuel
        else:
            distance = t - S[i]
            if distance > L: return -1
            refueled = distance - fuel

        total_cost += refueled * P[i]
        fuel += (refueled - distance)
        i = next_i
        
    return round(total_cost, 2)

L = 20
t = 125
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105, 112, 135, 140]
P = [3.2, 1.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .5, .2]
fuel = 4

print(tank(L, S, P, t, fuel))

L = 20
t = 126
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105, 112, 135, 140]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .5, .2]
fuel = 1

print(tank(L, S, P, t, fuel))

L = 20
t = 125
#    1    2    3    4    5    6    7    8    9    10    11   12   13   14   15   16   17   18   19    20   21   22
S = [1  , 9  , 21 , 30 , 35 , 39 , 41 , 42 , 50 , 58  , 62 , 80 , 85 , 92 , 97 , 98 , 100, 105, 112 , 113, 135, 140]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .1 , .5 , .2 ]
fuel = 15

print(tank(L, S, P, t, fuel))

L = 20
t = 132
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105, 112, 135, 140]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .5, .2]
fuel = 8

print(tank(L, S, P, t, fuel))

L = 20
t = 133
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18   19   20   21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105, 112, 135, 140]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2, 10.2, .5, .2]
fuel = 12

print(tank(L, S, P, t, fuel))

L = 20
t = 132
#    1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17   18
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 92, 97, 98, 100, 105]
P = [1.3, 3.2, 8.3, 8.1, 3.3, 5.2, 4.2, 6.7, 3.8, 10.3, 8.2, 3.8, 5.2, 2.9, 4.8, 3.2, 5.7, 1.2]
fuel = 15

print(tank(L, S, P, t, fuel))

L = 20
t = 30
S = [0,  1,   21, 22,  24, 25]
P = [10, 1.2, 5,  5.5, 5.1, 5]
fuel = 0

print(tank(L, S, P, t, fuel))