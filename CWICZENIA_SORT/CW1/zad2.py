class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def extract_max(head):
    guard=head
    maxi=head.next.val
    bmaxi=head

    while head.next != None:
        if head.next.val > maxi.val:
            bmaxi=head
            maxi=head.next
        head=head.next

    bmaxi.next=bmaxi.next.next
    return bmaxi.next

def extract_max_Falisz(L):
    maxi=L
    while L.next != None:
        if L.next.val > maxi.next.val:
            maxi=L

    ret = maxi.next
    maxi.next=ret.next
    ret.next=None
    return ret

def insert(head, node):
    guard=head

    while head.next != None and head.next.val <= node.val:
        head=head.next

    node.next=head.next
    head.next=node

def insertsort(head):
    newL=Node(None)
    while head.next != None:
        newN=Node(head.next.val)
        insert(newL,newN)
        head.next=head.next.next
        head=head.next
    head.next=newL.next

def selectsort(head):
    newL=Node(None)
    while head.next != None:
        newN=extract_max_Falisz(head)
        newN.next=newL.next
        newL.next=newN
    head.next=newL.next