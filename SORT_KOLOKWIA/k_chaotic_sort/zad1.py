from zad1testy import Node, runtests

def merge(a, b):
        res=None

        if a == None: return b
        if b == None: return a

        if a.val <= b.val:
            res = a
            res.next = merge(a.next, b)
        else:
            res = b
            res.next = merge(a, b.next)
    
        return res


def getMid(h):
    if h == None: return h

    slow = h
    fast = h

    while(fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeSorting(h):

    if h == None or h.next == None: return h

    mid =getMid(h)
    #print(mid.val)
    midNext = mid.next
    mid.next = None

    left = mergeSorting(h)
    right = mergeSorting(midNext)

        #self.wypisz()

    sortedL = merge(left, right)
    return sortedL

def SortH(p,k):
    if k == 0: return p
    return mergeSorting(p)


runtests( SortH ) 
