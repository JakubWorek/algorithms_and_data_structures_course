def unit_intervals(X: 'array of numbers'):
    n = len(X)
    if not X: return 0
    if n == 1: return 1
    
    X.sort()
    count = 1
    begin = X[0]
    for i in range(1, n):
        if X[i] <= begin + 1:
            continue
        count += 1
        begin = X[i]
        
    return count

X = [-.5, 0, .25, .5, 1.6, 1.8, 2.6]

print(unit_intervals(X))

X = [-.51, -.5, 0, .25, .5, 1.6, 1.8, 2.6]

print(unit_intervals(X))

X = [-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]
#                            ^  - modified
print(unit_intervals(X))