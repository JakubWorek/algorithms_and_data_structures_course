# Korzystając z własności drzewa binarnego odtwarzamy go
# do tablicy rosnąco.
# Następnie łączymy Node-y w tablicy w kolejności rosnącej
# tak jak w przypadku kopca binarnego

from zad1testy import runtests

def ConvertTree(p):
    # tu prosze wpisac wlasna implementacje
    def GetTab(node):
        if node.left: GetTab(node.left)
        nodes.append(node)
        if node.right: GetTab(node.right)
    
    nodes = []
    GetTab(p)
    n = len(nodes)

    for i in range(n):
        nodes[i].left = nodes[2*i+1] if 2*i+1 < n else None
        nodes[i].right = nodes[2*i+2] if 2*i+2 < n else None
        nodes[i].parent = nodes[(i-1)//2] if i > 0 else None

    return nodes[0]

runtests( ConvertTree )