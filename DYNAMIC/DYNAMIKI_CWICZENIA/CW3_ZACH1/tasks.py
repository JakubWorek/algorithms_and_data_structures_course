# Wybieramy najcenniejsze zadanie możliwe do wykonania
# Realizujemy je najpóźniej jak się da

def tasks(T: '(time limit, profit)'):
    # Sort all tasks by their profit
    T.sort(key=lambda task: task[1])
    # Get the max time limit possible
    limit = 0
    for task in T:
        if task[0] > limit:
            limit = task[0]
    # Create slots in which we will store information which
    # time periods are taken by more profitable tasks (do each task
    # the latest we can in order to leave some space for tasks which
    # need to be done earlier)
    result = []
    slots = [False] * limit
    for task in T:
        for i in range(task[0] - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                result.append(task)
                break
    return result

A = [[2, 50],
     [1, 21],
     [2, 27],
     [3, 25],
     [2, 15]
]

print(tasks(A))