from llist import Node, LList, append
from math import gcd

def cyclic(n):
    lst = LList()
    f = lambda x: (x*x+1) % n
    x = y = 2
    node = None
    for _ in range(n):
        x = f(x)
        y = f(f(y))
        if gcd(abs(x-y), n) != 1:
            node = Node(x)
            append(lst, node)
        else:
            append(lst, Node(x))
    append(lst, node)
    return lst

lst = cyclic(47077)
