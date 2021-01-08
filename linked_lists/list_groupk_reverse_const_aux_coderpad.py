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
        s = "{}->".format(self.val)
        s += "null" if not self.next else str(self.next)
        return s


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
            print("qapp", p.val, [qi.val for qi in q])
            p = p.next
            i += 1

        if not new_head:
            print("new head", q[-1])
            new_head = q[-1]

        for node in q[::-1]:
            if prev:
                prev.next = node

            prev = node

    node.next = None

    return new_head


def reverse_linked_list_in_groups_of_k2(head, k):
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


import random
import pytest


@pytest.mark.parametrize("i", range(100))
def test_list_build(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 10)
    arr = [rng.randint(0, 100) for _ in range(length)]
    lst = LinkedListNode.build(arr)
    s = str(lst)
    expected = "->".join([str(a) for a in arr])
    expected += "->null"
    assert s == expected


@pytest.mark.parametrize("arr,k,expected", [
    ([1, 2, 3, 4, 5, 6], 3, "3->2->1->6->5->4->null")
])
def test_reverse_linked_list_in_groups_of_k(arr, k, expected):
    lst = LinkedListNode.build(arr)
    lst2 = reverse_linked_list_in_groups_of_k(lst, 3)
    s = str(lst2)
    assert s == expected


@pytest.mark.parametrize("arr,k,expected", [
    ([1, 2, 3, 4, 5, 6], 3, "3->2->1->6->5->4->null")
])
def test_reverse_linked_list_in_groups_of_k2(arr, k, expected):
    lst = LinkedListNode.build(arr)
    lst2 = reverse_linked_list_in_groups_of_k2(lst, 3)
    s = str(lst2)
    assert s == expected


pytest.main()
