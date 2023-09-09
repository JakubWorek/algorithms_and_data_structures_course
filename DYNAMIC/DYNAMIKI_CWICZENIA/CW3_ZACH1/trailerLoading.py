# Sortujemy od najcięższych i ładujemy aż miejsce się skończy
# Zachłan działa tylko dla wag, które są potęgami tej samej liczby

def fill_the_trailer(W: 'weights of items', 
                     k: 'max possible total weight'):
    # Sort weights from the highest to the lowest
    W.sort(reverse=True)
    # Store items which were taken
    result = []
    for w in W:
        if w <= k:
            k -= w
            result.append(w)
    return result

W = [2, 2, 4, 8, 1, 8, 16]
k = 27

print(fill_the_trailer(W, k))