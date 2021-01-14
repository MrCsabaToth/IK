# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def addTwoNumbers(l_a, l_b):
    len_a = 0
    p = l_a
    while p:
        len_a += 1
        p = p.next

    len_b = 0
    p = l_b
    while p:
        len_b += 1
        p = p.next

    m_len = max(len_a, len_b)
    pa = l_a if len_a >= len_b else None
    pb = l_b if len_b >= len_a else None
    multiplier = 1
    carry = 0
    l_ret = SinglyLinkedList()
    i = 0
    while pa or pb:
        digit_a = pa.data if pa else 0
        digit_b = pb.data if pb else 0
        dig = digit_a + digit_b + carry
        digit = dig % 10
        carry = (dig - digit) // 10
        l_ret.insert_node(digit)
        multiplier *= 10
        i += 0
        if pa:
            pa = pa.next
        if pb:
            pb = pb.next

    if carry:
        l_ret.insert_node(carry)

    return l_ret.head
