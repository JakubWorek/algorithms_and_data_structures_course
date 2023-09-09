class Node:
    def __init__(self):
        self.cut    = None    # klucz tego wezla
        self.left   = None    # span = [self.left, self.right]
        self.right  = None
        self.intervals = []   # przedzialy zgromadzone w tym wezle
        self.lchild = None    # lewe dziecko
        self.rchild = None    # prawe dziecko
        self.leaf   = False   # czy to lisc?



# funkcja pomocnicza do budowania drzewa
def tree_build(A, i, j, left, right):
    X = Node()
    X.left  = left
    X.right = right
    if (j < i):
        # build leaf
        X.cut  = -1
        X.leaf = True
    else:
        # build internal node
        m = (i + j) // 2
        X.cut   = A[m]
        X.lchild = tree_build(A, i, m - 1, left, A[m])
        X.rchild = tree_build(A, m + 1, j, A[m], right)
    return X


# zbuduj drzewo przedzialowe, ktore moze przechowywac
# przedzialy postaci [a,b], gdzie a,b to punkty z tablicy A
# tablica A musi byc posortowana rosnaco i bez powtorzen
#
# Zlozonosc: O(n), gdzie n to rozmiar A
def tree(A):
    return tree_build(A,0,len(A)-1,min(A)-1, max(A)+1)





# Wypisz zawartosc drzewa X
def tree_print(X, ind=""):

    if X.leaf:
        print(ind, "leaf-span: [%d, %d] --> " % (X.left, X.right), X.intervals);
    if not X.leaf:
        print(ind, "cut = %d," % X.cut, "span = [%d, %d], " % (X.left, X.right), "intervals =", X.intervals);
        tree_print(X.lchild, ind + "  ")
        tree_print(X.rchild, ind + "  ")



# funkcja pomocnicza wykonujaca operacje na zadanym przedziale
def tree_op( X, I, f):
    (a, b) = I
    if a <= X.left and b >= X.right:
        f(X,I)
        return
    if a < X.cut:
        tree_op(X.lchild, I, f)
    if b > X.cut:
        tree_op(X.rchild, I, f)

# funkcja pomocnicza
def op_insert(X,I):
    X.intervals.append(I)

# funkcja pomocnicza
def op_remove( X, I ):
    try:
        X.intervals.remove(I)
    except ValueError:
        None



# Wstawia przedzial I do drzewa X
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_insert(X,I):
    tree_op( X, I, op_insert )

# Usuwa przedzial I z drzewa X (jesli przedzialu nie ma, to nic nie robi)
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_remove(X,I):
    tree_op( X, I, op_remove )




# zwraca liste wszystkich przedzialow z drzewa X, ktore zawieraja punkt a
# UWAGA: niektore przedzialy moga wystepowac dwa razy
#
# Dziala w czasie O(logn + k), gdzie n to liczba punktow na bazie
# ktorych powstalo drzewo a k to liczba znalezionych przedzialow
def tree_intersect(X, a):
    R = X.intervals.copy()
    if X.leaf:
        return R
    if a <= X.cut:
        R += tree_intersect(X.lchild, a)
    if a >= X.cut:
        R += tree_intersect(X.rchild, a)
    return R