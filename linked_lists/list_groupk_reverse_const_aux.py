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
    group_end = None
    prev_group_end = None

    while p:
        prev_group_end = group_end
        group_end = p
        i = 0
        while p and i < k:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
            i += 1

        if not new_head:
            new_head = prev

        if prev_group_end:
            prev_group_end.next = prev

    group_end.next = None

    return new_head
