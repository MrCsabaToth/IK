# For your reference:
#
# class SinglyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None
#         self.randomPointer = None
#
#     def set_randomPointer(self, randomPointer):
#         self.__randomPointer = randomPointer

def cloneLinkedList(head):
    p = head
    # 1. Insert cloned nodes into the original list
    while p:
        cloned = SinglyLinkedListNode(p.data)
        nxt = p.next
        p.next = cloned
        cloned.next = nxt
        p = nxt

    # 2. Wire in randomPointers by exploiting the brother original-cloned pairs
    p = head
    while p:
        if p.randomPointer:
            p.next.randomPointer = p.randomPointer.next

        p = p.next.next

    # 3. Detach the cloned nodes out fo the original list
    new_h = None
    new_tail = None
    p = head
    while p:
        if not new_h:
            new_h = p.next
            new_tail = p.next
        else:
            new_tail.next = p.next
            new_tail = new_tail.next

        p.next = p.next.next
        p = p.next

    return new_h
