from llist import *
from gencyclic import lst

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    node = lst.head
    counter = 0
    while counter < num and node.next:
        print(node.val)
        node = node.next
        counter+=1 
         

def find_cycle(lst):
    f = lambda node: node.next
    
    tortoise = f(lst.head) # f(x0) is the element/node next to x0.
    hare = f(f(lst.head))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Find the position μ of first repetition.    
    mu = 0
    tortoise = lst.head
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1
 
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
 
    return lam, mu


if __name__ == "__main__":
    tup = find_cycle(lst)
    print(f"cycle start: {tup[0]}")
    print(f" length: {tup[1]}")
