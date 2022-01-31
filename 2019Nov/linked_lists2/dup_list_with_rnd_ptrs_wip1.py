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
    new_h = None
    prev = None
    d = {}
    # 1. Duplicate list without randomPointers
    while p:
        n = SinglyLinkedListNode(p.data)
        d[p.data] = n
        if prev:
            prev.next = n

        if not new_h:
            new_h = n

        p = p.next
        prev = n

    # 2. Wire in randomPointers using the dictionary
    p1 = head
    p2 = new_h
    while p1:
        if p1.randomPointer:
            p2.randomPointer = d[p1.randomPointer.data]

        p1 = p1.next
        p2 = p2.next

    return new_h
