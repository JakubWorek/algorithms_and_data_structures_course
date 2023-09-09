import random

def find_sum_indices(arr, target_sum, k):
    i = 0
    j = len(arr) - 1
    
    while i < j:
        # Skip if i or j is an index of the value checked
        if i == k: 
            i += 1
            continue
        if j == k: 
            j -= 1
            continue
        
        curr_sum = arr[i] + arr[j]
        if curr_sum == target_sum: return i, j
        if curr_sum < target_sum: i += 1
        else: j -= 1
            
    return None, None

def runtests(f):
    # 1
    arr = [random.randint(-15, 15) for _ in range(random.randint(0, 20))]
    result = f(arr)

    print(sorted(arr))
    print(result)


    for k in range(len(arr)):
        i, j = find_sum_indices(arr, arr[k], k)
        print('Value:', arr[k], end='  ->\t')
        print(f'arr[i] = {arr[i]}, arr[j] = {arr[j]}' if i is not None else None)

    # 2
    arr = [0,0,0]
    result = f(arr)
    print(arr)
    print(result)

    for k in range(len(arr)):
        i, j = find_sum_indices(arr, arr[k], k)
        print('Value:', arr[k], end='  ->\t')
        print(f'arr[i] = {arr[i]}, arr[j] = {arr[j]}' if i is not None else None)