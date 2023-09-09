from zad2testy import runtests
from math import inf

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane

class Cache:
    def __init__(self, size):
        self.f = [None] * (size + 1)
        self.g = None

def valuableTree(T, k):
    if k == 0: return 0
    if k < 0 or not T: return None

    def f(root, t):
        # warunki końca:
        # 1. znaleźliśmy t-krawędziowe poddrzewo -> 0
        # 2. doszliśmy do liścia, ale nie mamy t krawędzi -> -inf
        if not t: return 0
        if not root: return -inf
        # Add cache object if there is no cache in the current subtree root
        if not root.X: root.X = Cache(k)
        # Check if we have already calculated the best k-edge subtree sum rooted
        # in the current node. If not, calculate the desired value.
        if root.X.f[t] is None:
            best = -inf
            if root.left:
                best = max(best, root.leftval + f(root.left, t - 1))
            if root.right:
                best = max(best, root.rightval + f(root.right, t - 1))
            if root.left and root.right and t >= 2:
                # i is a number of edges which we will look for in the left subtree.
                # (in the right subtree we have to look for t - 2 - i edges then)
                for i in range(t - 2 + 1):
                    curr = root.leftval + root.rightval + f(root.left, i) + f(root.right, t - 2 - i)
                    if curr > best:
                        best = curr
            root.X.f[t] = best
        # Return the max sum t-edges subtree sum
        return root.X.f[t]
    
    def g(root):
        # Return -inf if there is no root, that means there are no more edges
        # in the current subtree but we still have to find some edges. -inf is
        # a value that indicates that we haven't found enough edges in a subtree.
        if not root: return -inf
        # Add cache object if there is no cache in the current subtree root
        if not root.X: root.X = Cache(k)
        # Check if we have already calculated desired value. If not, we have to
        # recursively calculate the best subtree k-edges sum
        if root.X.g is None:
            # We can either include an edge (or both edges) connected to the current
            # root node (f function) or we can look for the best k-edges solution
            # in it'
            root.X.g = max(f(root, k), g(root.left), g(root.right))
        # Return the greatest sum obtained in a subtree
        return root.X.g

    return g(T)


def valuableTree_1(T, k):
    def f(node, i):
        nonlocal k
        if node is None: 
            return -inf
        if i == 0: 
            return 0
        if node.left is None and node.right is None and i != 0:
            return - inf
        if node.X is not None and node.X[i] is not None:
            return node.X[i]
        
        res = max(node.leftval + f(node.left, i-1), node.rightval + f(node.right, i-1))
        
        for j in range(i-1):
            res = max(res, node.leftval+node.rightval+f(node.left, j)+f(node.right, i-2-j))
        
        if node.X is None: node.X = [None]*(k+1)
        node.X[i] = res
        return node.X[i]


    def getSol(root, k):
        nonlocal sol
        res = f(root, k)
        sol = max(sol, res)
        if root.left is not None: getSol(root.left, k)
        if root.right is not None: getSol(root.right, k)


    sol = -inf
    getSol(T,k)
    return sol


runtests(valuableTree_1)