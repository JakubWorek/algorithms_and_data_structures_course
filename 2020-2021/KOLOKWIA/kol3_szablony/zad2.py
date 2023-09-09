from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def leaf(node):
    if node.left is None and node.right is None:
        return True
    return False

def cutthetree(T):
    def dfs(root):
        if (root.left and leaf(root.left)) or\
            (root.right and leaf(root.right)):
            return root.value

        res = root.value

        if root.left is not None and root.right is None:
            res = min(res, dfs(root.left))
        elif root.left is None and root.right is not None:
            res = min(res, dfs(root.right))
        else:
            res = min(res, dfs(root.left)+dfs(root.right))
        return res
    
    return dfs(T.left) + dfs(T.right)

    
runtests(cutthetree)


