# 1) łączna liczba tankowań minimalna
# zachłan, za każdym razem max odległość przebywamy
# i za każdym razem tankujemy do pełna

def tank(L: 'capacity of tank of a tank',
         S: 'array with distances of stations from the starting point',
         t: 'distance to the target point',
         fuel: 'initial amount of fuel'):
    # S.sort()  # Uncomment this line if an array of stations isn't sorted
    # If a tank can reach the target point without refueling, return 0
    if fuel >= t: return 0
    if S[0] > fuel: return -1
    
    n = len(S)
    # Check if we can get to each station on the way
    if L < S[0] or t - S[-1] > L: return -1
    for i in range(1, n):
        if S[i] >= t:
            break
        if S[i] - S[i - 1] > L:
            return -1
    
    # Add a sentinel station if necessary
    if S[-1] < t:
        S.append(float('inf'))
    
    # Find the first station
    count = 1
    i = 0
    while i < n and S[i] <= fuel:
        i += 1
        
    i -= 1
    tank_pos = S[i]
    print(f'0 -> {S[i]}')
    
    while i < n + 1:
        # If S[i] is too far to reach, we have to refuel on the S[i - 1] station
        if S[i] - tank_pos > L:  # <--- sentinel station will be useful here
            print(f'{tank_pos} -> {S[i - 1]}')
            count += 1
            tank_pos = S[i - 1]
        if S[i] >= t:
            break
        i += 1
        
    # Remove a sentinel station
    S.pop()
    
    return count if t - tank_pos <= L else -1

L = 25
t = 105
#    0, 1, 2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17,  18,  19,  20,  21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 130, 135]
#       ^  ^               ^           ^   ^   ^                       ^
fuel = 21
print(tank(L, S, t, fuel))

L = 20
t = 133
#    0, 1, 2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17,  18,  19,  20,  21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140, 160, 190]
#   impossible -------------------------------------------------------------------^----^
fuel = 1
print(tank(L, S, t, fuel))

L = 20
t = 14
#    0, 1, 2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17,  18,  19,  20,  21
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 15
#   no tanking
print(tank(L, S, t, fuel))

L = 5
t = 21
S = [0, 2, 3, 5, 8, 11, 13, 17]
fuel = 5

print(tank(L, S, t, fuel))