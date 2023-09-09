class item():
    def __init__(self):
        self.value = None
        self.weight = None
        self.height = None

def knapsack_2d(Items, W, H):

    n = len(Items)
    F = [[[0 for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]

    for w in range(Items[0].weight, W + 1):
        for h in range(Items[0].height, H + 1):
            F[0][w][h] = Items[0].value

    for i in range(1, n):
        for w in range(1, W+1):
            for h in range(1, H+1):
                F[i][w][h] = F[i-1][w][h]

                if h >= Items[i].height and w >= Items[i].weight:
                    F[i][w][h] = max(F[i-1][w][h], F[i-1][w - Items[i].weight][h - Items[i].height] + Items[i].value)

    return F[n-1][W][H]

def modify(P, W, H):
    n = len(P)
    T = [item() for _ in range(n)]
    for i in range(n):
        T[i].value = P[i]
        T[i].weight = W[i]
        T[i].height = H[i]
    return T

P1 = [4, 10, 2, 3, 8]
W1 = [10, 6, 1, 2, 6]
H1 = [3, 9, 12, 4, 9]

P2 = [4, 10, 2, 3, 8]
W2 = [10, 4, 1, 2, 6]
H2 = [3, 9, 12, 4, 2]

MaxW = 12
MaxH = 20

Items1 = modify(P1, W1, H1)
print(knapsack_2d(Items1, MaxW, MaxH))

Items2 = modify(P2, W2, H2)
# knapsack_2d(Items2, MaxW, MaxH)