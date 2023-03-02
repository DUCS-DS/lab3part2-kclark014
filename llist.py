class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LList:
    def __init__(self):
        self.head = None

def append(lst, newnode):
    """append newnode to (finite) linked list lst"""
    if lst.head:
        node = lst.head
        while node.next:
            node = node.next
        node.next = newnode
    else:
        lst.head = newnode
