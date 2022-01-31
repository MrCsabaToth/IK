'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def reverse_linked_list_in_groups_of_k(head, k):
    p = head
    prev = None
    new_head = None
    node = None
    while p:
        i = 0
        q = []
        while i < k and p:
            q.append(p)
            p = p.next
            i += 1

        if not new_head:
            new_head = q[-1]

        for node in q[::-1]:
            if prev:
                prev.next = node

            prev = node

    node.next = None

    return new_head
