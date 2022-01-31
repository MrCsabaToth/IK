# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def addTwoNumbers(l_a, l_b):
    pa = l_a
    pb = l_b
    carry = 0
    l_ret = SinglyLinkedList()
    while pa or pb:
        digit_a = pa.data if pa else 0
        digit_b = pb.data if pb else 0
        dig = digit_a + digit_b + carry
        if dig < 10:
            digit = dig
            carry = 0
        else:
            digit = dig - 10
            carry = 1

        l_ret.insert_node(digit)
        if pa:
            pa = pa.next
        if pb:
            pb = pb.next

    if carry:
        l_ret.insert_node(carry)

    return l_ret.head
