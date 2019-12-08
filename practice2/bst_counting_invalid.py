# Doesn't filter enough
# Apparently I count some dups
def how_many_BSTs(n):
    tree = [None] * (2 ** n)

    def bst_helper(partial, initial):
        if not partial:
            return 1

        # 1. pick the next element
        cnt = 0
        for elem in partial[:]:
            print("pick " + str(elem))
            if initial:
                tree[1] = elem
                partial.remove(elem)
                cnt += bst_helper(partial, False)
                partial.append(elem)
                tree[1] = None
            else:
                # 2. Iterate through potential placements which don't violate BST 
                for idx, node in enumerate(tree):
                    if node is None or not idx:
                        continue
    
                    idx2 = idx * 2
                    idx3 = None
                    if node > elem and tree[idx2] is None:
                        idx3 = idx2
                    if node < elem and tree[idx2 + 1] is None:
                        idx3 = idx2 + 1

                    if idx3 is not None:
                        tree[idx3] = elem
                        partial.remove(elem)
                        cnt += bst_helper(partial, False)
                        partial.append(elem)
                        tree[idx3] = None

        return cnt

    return bst_helper(list(range(1, n + 1)), True)


import pytest


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
])
def test_bst(n, expected):
    assert(how_many_BSTs(n)) == expected


pytest.main()
