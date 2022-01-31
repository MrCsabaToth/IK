#Reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}
def find_middle_node(head):
    if not head:
        return None

    node = head
    mid = node
    i = 0
    while node.next:
        if not i % 2:
            mid = mid.next

        node = node.next
        i += 1

    return mid
