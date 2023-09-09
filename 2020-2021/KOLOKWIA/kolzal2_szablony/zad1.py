# f(i) - funkcja określająca który spośród 0...i prostokąt
# należy usunąć, aby pole przecięcia pozostałych było największe
# wynik programu to f(n)
#
# Pierwsze 3 prostokąty sprawdzamy "ręcznie" i wybieramy ten, który 
# najbardziej opłaca się usunąć.
# Kolejne wartości obliczamy sprawdzając, czy bardziej opłaca się usunąć
# obecznie sprawdzany prostokąt (i), czy usunąć poprzednio wybrany (to_remove) 

from zad1testy import runtests
from math import inf

def cut(rec1, rec2):
    x11, y11, x12, y12 = rec1
    x21, y21, x22, y22 = rec2
    x1 = max(x11, x21)
    y1 = max(y11, y21)
    x2 = min(x12, x22)
    y2 = min(y12, y22)
    return x1, y1, x2, y2

def area(x1, y1, x2, y2):
    return (x2-x1) * (y2-y1)

def rect(D):
    """tu prosze wpisac wlasna implementacje"""
    n = len(D)
    if n<3: return None

    # sprwdzamy pierwsze 3 prostokąty
                                    # usuwamy    0     1     2
    cuts = [area(*cut(D[i], D[j])) for i,j in ((1,2),(0,2),(0,1))]
    to_remove = cuts.index(max(cuts))
    remaining = [0,1,2]
    remaining.remove(to_remove)
    cut_cords = cut(D[remaining[0]], D[remaining[1]])

    # sprawdzamy pozostałe
    for i in range(3, n):
        # jeżeli usuwamy i-ty prostokąt
        curr_cut_cords = cut(cut_cords, D[to_remove])
        curr_area = area(*curr_cut_cords)
        # a jeżeli usuwamy wcześniej wybrany
        prev_cut_cords = cut(cut_cords, D[i])
        prev_area = area(*prev_cut_cords)

        # wybieramy lepszy
        if curr_area > prev_area:
            cut_cords = curr_cut_cords
            to_remove = i
        else: cut_cords = prev_cut_cords

    return to_remove


def rect2(D):
    max_left = -inf
    prev_max_left = -inf
    min_right = inf
    prev_min_right = inf
    max_down = -inf
    prev_max_down = -inf
    min_up = inf
    prev_min_up = inf

    for x1, y1, x2, y2 in D:
        if x1 > max_left:
            prev_max_left = max_left
            max_left = x1
        elif x1 > prev_max_left:
            prev_max_left = x1
        if x2 < min_right:
            prev_min_right = min_right
            min_right = x2
        elif x2 < prev_min_right:
            prev_min_right = x2
        if y1 > max_down:
            prev_max_down = max_down
            max_down = y1
        elif y1 > prev_max_down:
            prev_max_down = y1
        if y2 < min_up:
            prev_min_up = min_up
            min_up = y2
        elif y2 < prev_min_up:
            prev_min_up = y2

    best_rect = None
    if max_left > min_right or max_down > min_up:
        area = 0
    else:
        area = (min_right - max_left) * (min_up - max_down)

    n = len(D)

    for i in range(n):
        x1, y1, x2, y2 = D[i]
        new_x1 = max_left
        if x1 == max_left:
            new_x1 = prev_max_left

        new_x2 = min_right
        if x2 == min_right:
            new_x2 = prev_min_right

        new_y1 = max_down
        if y1 == max_down:
            new_y1 = prev_max_down

        new_y2 = min_up
        if y2 == min_up:
            new_y2 = prev_min_up

        if new_x1 > new_x2 or new_y1 > new_y2:
            new_area = 0
        else:
            new_area = (new_x2 - new_x1) * (new_y2 - new_y1)

        if best_rect is None and new_area == area:
            best_rect = i
        if new_area > area:
            area = new_area
            best_rect = i

    return best_rect

runtests( rect )


