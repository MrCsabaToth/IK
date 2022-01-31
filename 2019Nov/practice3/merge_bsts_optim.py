# Optimization: don't instanciate Nodes
def traverseInOrder(node):
    if not node:
        return []

    traversal = traverseInOrder(node.left)
    traversal.append(node)
    traversal.extend(traverseInOrder(node.right))
    return traversal


def mergeSorted(a, b):
    aptr = 0
    alen = len(a)
    bptr = 0
    blen = len(b)
    merged = [None] * (alen + blen)
    i = 0
    while aptr < alen or bptr < blen:
        if bptr >= blen or aptr < alen and a[aptr].key < b[bptr].key:
            merged[i] = a[aptr]
            aptr += 1
        else:
            merged[i] = b[bptr]
            bptr += 1
        i += 1

    return merged, (alen + blen)


def buildBalancedBSTFromSorted(arr, start, end):
    if start > end:
        return None

    # Overflow of "(start + end) // 2" avoided - Omkar
    mid = start + (end - start) // 2
    node = arr[mid]
    node.left = buildBalancedBSTFromSorted(arr, start, mid - 1)
    node.right = buildBalancedBSTFromSorted(arr, mid + 1, end)
    return node


# Complete this function and return root of the BST
def mergeTwoBSTs(root1, root2):
    # 1. Traverse root1 in-order (sorted outcome)
    trav1 = traverseInOrder(root1)
    # 2. Traverse root2 in-order (sorted outcome)
    trav2 = traverseInOrder(root2)
    # 3. Merge root1 + root2
    merged, length = mergeSorted(trav1, trav2)
    # 4. Build balanced BST from sorted array
    return buildBalancedBSTFromSorted(merged, 0, length - 1)
