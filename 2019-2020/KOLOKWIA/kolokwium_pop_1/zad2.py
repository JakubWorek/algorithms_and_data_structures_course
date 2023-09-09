from zad2testy import runtests

def fast_list_prepend(L,a):
    # tu prosze wpisac wlasna implementacje
    if not L: return FastListNode(a)
    node = FastListNode(a)
    node.next.append(L)

    curr = L
    i = 0
    while i < len(curr.next):
        node.next.append(curr.next[i])
        curr = curr.next[i]
        i += 1

    print_list(node)
    return node


def print_list(L):
    curr = L
    while True:
        print(curr)
        if not curr.next: break
        curr = curr.next[0]


class FastListNode:
  def __init__(self, a):
    self.a = a     # przechowywana liczba calkowita
    self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

  def __str__(self): # zwraca zawartosc wezla w postaci napisu
    res = 'a: ' + str(self.a) + '\t' + 'next keys: '
    res += str([n.a for n in self.next])
    return res




runtests( fast_list_prepend ) 
