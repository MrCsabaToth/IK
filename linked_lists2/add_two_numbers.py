# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def addTwoNumbers(l_a, l_b):
    pa_prev = None
    pa = l_a
    pb_prev = None
    pb = l_b
    carry = 0
    derail = False
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

        if pa:
            pa.data = digit
            if not pa.next and pb and pb.next:
                pa.next = pb.next
                derail = True
                pa = None
            else:
                pa_prev = pa
                pa = pa.next

        if pb:
            if derail:
                pb.data = digit

            pb_prev = pb
            pb = pb.next

    if carry:
        last = SinglyLinkedListNode(carry)
        if derail:
            pb_prev.next = last
        else:
            pa_prev.next = last

    return l_a
