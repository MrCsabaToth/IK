class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

    @staticmethod
    def build(arr):
        next = None
        for a in arr[::-1]:
            node = LinkedListNode(a)
            node.next = next
            next = node

        return node

    def __str__(self):
        s = "{}".format(self.val)
        if self.next:
            s += "," + str(self.next)

        return s


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

    print("#1", str(mid))
    if not i % 2:
        midprev = mid
        mid = mid.next

    print("#12", str(mid))
    midprev.next = None
    print("#13", str(head))

    # 2. Reverse second half: O(n)
    p = mid
    prev = None

    while p:
        nxt = p.next
        p.next = prev
        prev = p
        p = nxt

    print("#21", str(prev))
    print("#22", str(head))

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


import pytest
import random


@pytest.mark.parametrize("i", range(10))
def test_list_build(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 10)
    arr = [rng.randint(0, 100) for _ in range(length)]
    lst = LinkedListNode.build(arr)
    s = str(lst)
    expected = ",".join([str(a) for a in arr])
    assert s == expected


@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3, 4, 5, 6], "1,6,2,5,3,4"),
])
def test_zip_given_linked_list(arr, expected):
    lst = LinkedListNode.build(arr)
    lst2 = zip_given_linked_list(lst)
    s = str(lst2)
    assert s == expected


pytest.main()
