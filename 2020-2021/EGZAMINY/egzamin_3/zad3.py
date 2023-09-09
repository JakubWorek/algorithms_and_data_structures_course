from zad3testy import runtests

# gorsza złożoność, po prostu odczytuje wartości z drzewa
# i wstawiam do tablicy
def maxim( T, C ):
    def GetHeight(T):
        h = 0
        curr = T
        while curr:
            curr = curr.right
            h += 1
        return h
    
    def GetTab(node,idx):
        nodes[idx] = node.key
        if node.left: GetTab(node.left, 2*idx)
        if node.right: GetTab(node.right, 2*idx + 1)
    
    nodes = [None]*(2**GetHeight(T))
    GetTab(T,1)
    return max(nodes[i] for i in C)
    
runtests( maxim )


