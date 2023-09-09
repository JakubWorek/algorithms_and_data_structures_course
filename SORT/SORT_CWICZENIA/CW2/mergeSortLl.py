from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def dodaj(self,newVal):

        newNode = Node(newVal)

        if self.head is None:
            self.head = newNode
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = newNode


    def wypisz(self):
        if self.head is None:
            print("Nothing to be printed")
            return
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next

        print(" ")


    def merge(self, a, b):
        res=None

        if a == None: return b
        if b == None: return a

        if a.val <= b.val:
            res = a
            res.next = self.merge(a.next, b)
        else:
            res = b
            res.next = self.merge(a, b.next)
    
        return res


    def getMid(self, h):
        if h == None: return h

        slow = h
        fast = h

        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow


    def mergeSorting(self, h):

        if h == None or h.next == None: return h

        mid = self.getMid(h)
        #print(mid.val)
        midNext = mid.next
        mid.next = None

        left = self.mergeSorting(h)
        right = self.mergeSorting(midNext)

        #self.wypisz()

        sortedL = self.merge(left, right)
        return sortedL


    def mergeSort(self):
        self.head = self.mergeSorting(self.head)


def main():
    ll=LinkedList()

    for i in range(10):
        num=randint(1,100)
        ll.dodaj(num)
    
    ll.wypisz()
    ll.mergeSort()
    ll.wypisz()

if __name__ == '__main__': main()