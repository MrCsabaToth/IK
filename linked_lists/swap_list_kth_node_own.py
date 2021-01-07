'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def swap_nodes(head, k):
    p1 = head
    p1p = None
    for _ in range(k - 1):
        p1p = p1
        p1 = p1.next
        if not p1:
            break

    p2 = head
    p2p = None
    p12 = p1.next
    j = 1
    while p12:
        p12 = p12.next
        p2p = p2
        p2 = p2.next
        j += 1

    if p1 is p2:
        return head

    if j >= k:
        ret = p2 if p1 is head else head

        if p2p:
            p2p.next = p1
        p1n = p1.next
        p1.next = p2.next
        if p1 is not head:
            p1p.next = p2

        p2.next = p1n
    else:
        ret = p1 if p2 is head else head

        if p1p:
            p1p.next = p2
        p2n = p2.next
        p2.next = p1.next
        if p2 is not head:
            p2p.next = p1

        p1.next = p2n

    return ret
