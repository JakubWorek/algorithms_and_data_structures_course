import random

def runtests(f):
    arr = [random.randint(1,1000) * 75 + 150 for _ in range(random.randint(1, 100))]
    p = random.randrange(len(arr))
    q = random.randrange(p, len(arr))

    expected_result = sorted(arr)[p:q+1]
    result = f(arr, p, q)

    print('Result:')
    print(result, end='\n\n')
    print('Expected:')
    print(expected_result)
    print('\nIs correct?', expected_result == result)