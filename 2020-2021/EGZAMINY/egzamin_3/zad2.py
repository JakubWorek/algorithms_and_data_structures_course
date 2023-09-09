# Drzewo prefiksowe

from zad2testy import runtests

class Node():
    def __init__(self):
        self.isPrefix = False
        self.left = None
        self.right = None
        self.parent = None

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        curr = self.root

        for c in string:
            if c == '0':
                if curr.left: curr.left.isPrefix = True
                else:
                    curr.left = Node()
                    curr.left.parent = curr
                curr = curr.left
            else:
                if curr.right: curr.right.isPrefix = True
                else:
                    curr.right = Node()
                    curr.right.parent = curr
                curr = curr.right

    def getPrefixes(self):
        leaves = self.getPrefixLeaves()
        prefixes = []
        for node in leaves:
            prefixes.append(self.getPrefix(node))

        #print(prefixes)
        return prefixes
    
    def getPrefixLeaves(self):
        leaves = []

        def dfs(node):
            isLeaf = True
            if node.left and node.left.isPrefix:
                isLeaf = False
                dfs(node.left)
            if node.right and node.right.isPrefix:
                isLeaf = False
                dfs(node.right)
            if isLeaf: leaves.append(node)

        dfs(self.root)
        return leaves
    
    def getPrefix(self, node):
        chars = []

        while node.parent:
            if node.parent.left is node:
                chars.append('0')
            else: chars.append('1')
            node = node.parent

        chars.reverse()
        return ''.join(chars)


def double_prefix( L ):
    """tu prosze wpisac wlasna implementacje"""
    Tree = PrefixTree()
    for string in L: Tree.insert(string)
    return Tree.getPrefixes()


runtests( double_prefix )

