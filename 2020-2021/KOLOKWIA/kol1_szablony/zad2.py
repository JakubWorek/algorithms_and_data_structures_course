from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 

def merge(first1,first2):
    wsk1 = first1
    wsk2 = first2
    first3 = None
    if wsk1 is None:
        return first2
    if wsk2 is None:
        return first1
    if wsk1.val > wsk2.val:
        first3 = wsk2
        wsk2 = wsk2.next
        first3.next = None
    else:
        first3 = wsk1
        wsk1 = wsk1.next
        first3.next = None
    currNode = first3
    while wsk1 is not None and wsk2 is not None:
        if wsk1.val > wsk2.val:
            currNode.next = wsk2
            wsk2 = wsk2.next
            currNode = currNode.next
        else:
            currNode.next = wsk1
            wsk1 = wsk1.next
            currNode = currNode.next
    if wsk1 is not None:
        currNode.next = wsk1
    if wsk2 is not None:
        currNode.next = wsk2
    return first3

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

def insertion_sort(first,k):
    guard = Node()
    guard.next = first
    prevNode = first
    currNode = prevNode.next
    i = 0
    edge = guard
    while currNode is not None:
        if i > k:
            edge = edge.next
        if currNode.val >= prevNode.val:
            prevNode = currNode
            currNode = currNode.next
        else:
            pos = edge
            while currNode.val > pos.next.val:
                pos = pos.next
            prevNode.next = currNode.next
            currNode.next = pos.next
            pos.next = currNode
            currNode = prevNode.next
        i +=1
    return guard.next

def SortH(p,k):
    if k == 0: return p
    if k <= 10: return insertion_sort(p,k)
    return mergeSorting(p)


runtests( SortH ) 