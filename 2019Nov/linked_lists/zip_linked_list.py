'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def zip_given_linked_list(head):
    # 1. Determine middle node O(n)
    if not head:
        return None

    node = head
    mid = node
    midprev = None
    i = 0
    while node.next:
        if not i % 2:
            midprev = mid
            mid = mid.next

        node = node.next
        i += 1

    if not i % 2:
        midprev = mid
        mid = mid.next

    midprev.next = None

    # 2. Reverse second half: O(n)
    p = mid
    prev = None

    while p:
        nxt = p.next
        p.next = prev
        prev = p
        p = nxt

    # 3. Zip: O(n)
    p = head
    r = prev
    while p:
        nxt = p.next
        rxt = r.next if r else None
        p.next = r
        if r:
            r.next = nxt
        r = rxt
        p = nxt

    return head
