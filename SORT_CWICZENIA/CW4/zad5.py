def max_span(T):
    minimum = maximum = T[0]
    for i in range(1, len(T)):
        maximum = max(maximum, T[i])
        minimum = min(minimum, T[i])
    A = [[] for _ in range(len(T))]
    x = (maximum + minimum) / len(T)
    for i in range(len(T)):
        bucket_num = int((T[i] - minimum) / x)
        A[bucket_num].append(T[i])
    result = 0
    prev_maximum = max(A[0])
    best_numbers = 0
    for i in range(1, len(T)):
        if len(A[i]) == 0:
            continue
        else:
            actual_minimum = min(A[i])
            if actual_minimum - prev_maximum > result:
                best_numbers = (actual_minimum, prev_maximum)
                result = actual_minimum - prev_maximum
            prev_maximum = max(A[i])
    return result, best_numbers