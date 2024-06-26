from pprint import pprint

T0 = [
    [1, 0],
    [0, 0],
]

T1 = [
    [3, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T2 = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

T3 = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

r0_T4 = [6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1]
T4 = [
         r0_T4
     ] + (
             [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (len(r0_T4) - 1)
     )

T5 = [
    [1, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

T6 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T7 = [
    [5, 0, 1, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
]

TESTS = [
    (T0, [0]),
    (T1, [0, 3]),
    (T2, [0, 4]),
    (T3, [0, 2]),
    (T4, [0, 2, 4]),
    (T5, [0, 2, 7]),
    (T6, [0]),
    (T7, [0, 5]),
]


def runtests(f):
    OK = True
    for no, (T, expected) in enumerate(TESTS):
        print(f"---------------------- #{no}")
        print("T: ")
        pprint(T)
        print(f"oczekiwany wynik: {expected}")
        assert all(len(T[i]) == len(T) for i in range(len(T))), f"len(T): {len(T)}, len(T[0]): {len(T[0])}"
        actual = f(T)
        print(f"uzyskany wynik  : {actual}")
        if actual != expected:
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")