from egzP4btesty import runtests 
from bisect import bisect

class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None

def walk(root, tab):
    if root.left:
        walk(root.left, tab)
    tab.append(root.key)
    if root.right:
        walk(root.right, tab)

def sol(root, T):
    valT = []
    walk(root, valT)

    res = 0
    for el in T:
        x = bisect(valT, el.key -1 )
        if valT[x-1] + valT[x+1] == 2*valT[x]:
            res += valT[x]
    return res
    
runtests(sol, all_tests = True)