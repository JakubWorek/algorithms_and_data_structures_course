class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(a,b):
    l=Node(None)
    h=l
    while a.next is not None and b.next.next is not None:
        if a.next.val > b.next.val:
            l.next=b.next
            b=b.next
            l=l.next
        else:
            l.next=a.next
            a=a.next
            l=l.next

    if a.next is not None:
        l.next=a
    else:
        l.next=b
    
    return h


def sortowanie(l):
    head = Node(None)
    cnt=0
    while True:
        while l.next is not None:
            a1=l
            a2=l
            while a1.next is not None and a2.val<a2.next.val:
                a2=a2.next
            l=a2.next
            cnt+=1
            a2.next=None
            if l==None and cnt==1:
                return a1
            b1=l
            b2=l
            while b1.next is not None and b2.next.val<b2.next.next.val:
                b2=b2.next
            b2.next=None
            
