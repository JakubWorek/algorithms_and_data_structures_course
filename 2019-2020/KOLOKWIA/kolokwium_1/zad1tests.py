import random

random.seed(0)

def runtests(f):
    arr = [random.randint(0, 1_000_000) for _ in range(random.randint(0, 25))]
    print('Input arr:', arr, sep='\n', end='\n\n')
    f(arr)
    print('Result:', arr, sep='\n', end='\n\n')

