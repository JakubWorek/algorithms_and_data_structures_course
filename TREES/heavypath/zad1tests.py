class Node:
    def __init__(self):
        self.children = 0
        self.child = []

def runtests(f):
    A = Node()
    B = Node()
    C = Node()
    A.children = 2
    A.child = [(B, 5), (C, -1)]
    print(f(A))