from egz1btesty import runtests

class Node:
    def __init__( self ):
        self.left = None    # lewe poddrzewo
        self.right = None   # prawe poddrzewo
        self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    # wyliczmy wyskość
    T.x = [None, False]
    h=-1
    def height( R, level):
        nonlocal h
        h = max(h, level)
        if R.left is not None:
            R.left.x = [R, False]
            height( R.left, level+1 )
        if R.right is not None:
            R.right.x = [R, False]
            height( R.right, level+1 )
    height( T, 0 )

    # wyznaczamy ile liści jest na danym poziomie drzewa
    leafs = [[i] for i in range(h+1)]
    def putLeaves(R, level):
        nonlocal leafs
        leafs[level].append(R)
        if R.left is not None:
            putLeaves(R.left, level + 1)
        if R.right is not None:
            putLeaves(R.right, level + 1)
    putLeaves(T, 0)

    # wybieram od największej liczby liści na największej wysokości
    leafs.sort(key=lambda x: (len(x), x[0]), reverse=True)

    # przechodzimy po liściach i odcinamy ich dzieci zliczając
    # ilość uciętych krawędzi,
    # z każdego liścia idziemy do góry zaznaczając drogę
    # do głównego korzenia (flag = True)
    def paths(R):
        if R.x[1] is True: return
        if R.x[0] is not None:
            R.x[1] = True
            paths(R.x[0])
    
    ans = 0
    for node in leafs[0][1:]:
        paths(node)
        if node.left is not None:
            node.left = None
            ans +=1
        if node.right is not None:
            node.right = None
            ans +=1
    
    # schodzimy w dół jeżeli jest dziecko i ma flagę True
    # a jeżeli dziecko ma flagę False to jest do ucięcia
    # i zwiększamy ans

    def erase(R):
        nonlocal ans
        if R.left is not None:
            if R.left.x[1] is True: erase(R.left)
            else:
                ans+=1
                R.left = None
        if R.right is not None:
            if R.right.x[1] is True: erase(R.right)
            else:
                ans+=1
                R.right = None
    
    erase(T)

    return ans

#########################################################
def count_on_level(T):
        levels = []
        def visit(R, level):
            if len(levels) == level: levels.append(1)
            else: levels[level] += 1

            if R.left:
                visit(R.left, level+1)
            if R.right:
                visit(R.right, level+1)

        visit(T, 0)
        return levels

def visit(T, max_level):
    def dfs(node, lvl):
        if node is None: return
        if node.left: dfs(node.left, lvl+1)
        if node.right: dfs(node.right, lvl+1)

        if node.left is None and node.right is None:
            node.x = True
        else:
            if node.left is not None and node.right is not None:
                node.x = node.left.x and node.right.x
            elif node.left is not None:
                node.x = node.left.x
            else: node.x = node.right.x

        if lvl == max_level: node.x = False

    dfs(T, 0)

def erase(T):
    res = 0
    def visit(node):
        nonlocal res
        if node.x: res += 1
        else:
            if node.right is not None:
                visit(node.right)
            if node.left is not None:
                visit(node.left)

    visit(T)
    return res

def wideentall_1(T):
    levels = count_on_level(T)
    n = len(levels)
    max_level = n-1
    max_val = levels[-1]
    for i in range(n-1, -1, -1):
        if levels[i] > max_val:
            max_level = i
            max_val = levels[i]

    visit(T, max_level)
    sol = erase(T)
    return sol

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall_1, all_tests = False )