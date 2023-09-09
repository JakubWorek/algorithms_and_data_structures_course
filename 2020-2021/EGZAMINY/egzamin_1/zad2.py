from zad2testy import runtests
from queue import PriorityQueue


def robot( L, A, B ):
    # 3 poziomy przyspieszenia, 4 możliwe kierunki, szerokość labiryntu, wysokość labiryntu
    DP = [[[[-1] * 3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    
    queue = PriorityQueue()
    # czas, położenie x, położenie y, kierunek, poziom przyspieszenia
    queue.put((0, A[0], A[1], 0, 0))

    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]

    while not queue.empty():
        time, x, y, direction, idx = queue.get()
        if (x, y) == B:
            return time
        if DP[y][x][direction][idx] != -1 or L[y][x] == 'X':
            continue
        DP[y][x][direction][idx] = time
        queue.put((time + 45, x, y, (direction + 1) % 4, 0))
        queue.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        queue.put((time + seconds[idx], x, y, direction, min(idx + 1, 2)))
    return None


runtests( robot )


