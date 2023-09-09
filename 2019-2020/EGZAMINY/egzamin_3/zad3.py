# Złożoność: O(nlogn)

from zad3testy import runtests
from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def addSentinels(L):
    n = len(L)
    for i in range(n):
        sent = Node(None)
        sent.next = L[i]
        L[i] = sent

def getLength(head):
    _len = 0
    curr = head.next
    while curr:
        _len += 1
        curr = curr.next
    return _len

def merge(head1, head2):
    curr1 = head1.next
    curr2 = head2.next
    head = tail = Node(None)

    while curr1 and curr2:
        if curr1.val < curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next
    
    if curr1: tail.next = curr1
    else: tail.next = curr2

    return head

def merge_lists(L):
    # tu prosze wpisac implementacje
    n = len(L)
    if not L: return None
    if n == 1: return L[0]

    addSentinels(L)
    Q = PriorityQueue()
    for i in range(n):
        Q.put((getLength(L[i]), i, L[i]))

    i = n
    while True:
        len1, _, head1 = Q.get()
        len2, _, head2 = Q.get()
        newHead = merge(head1, head2)
        newLen = len1 + len2

        if not Q.empty():
            Q.put((newLen, i, newHead))
            i+=1
        else: return newHead.next


runtests( merge_lists )