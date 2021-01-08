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


pytest.main()
