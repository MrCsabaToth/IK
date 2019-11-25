# The is_valid now check all the way to the root
# Still I count more variations than intended
def how_many_BSTs(n):
    tree = [None] * (2 ** n)

    def is_valid(idx, elem):
        valid = True
        while valid:
            left = idx % 2 == 0
            idx = idx // 2
            parent = tree[idx]
            valid = valid and parent > elem and left or parent < elem and not left
            if not valid or idx <= 1:
                break

        return valid

    def bst_helper(pool, leafs, initial):
        if not pool:
            print("found " + str(tree))
            return 1

        # 1. pick the next element
        cnt = 0
        for elem in pool[:]:
            if initial:
                tree[1] = elem
                pool.remove(elem)
                leafs.extend([2, 3])
                cnt += bst_helper(pool, leafs, False)
                leafs.remove(2)
                leafs.remove(3)
                pool.append(elem)
                tree[1] = None
            else:
                # 2. Iterate through potential placements which don't violate BST 
                for leaf in leafs[:]:
                    if is_valid(leaf, elem):
                        tree[leaf] = elem
                        pool.remove(elem)
                        leafs.remove(leaf)
                        leafs.extend([leaf * 2, leaf * 2 + 1])
                        cnt += bst_helper(pool, leafs, False)
                        leafs.remove(leaf * 2)
                        leafs.remove(leaf * 2 + 1)
                        leafs.append(leaf)
                        pool.append(elem)
                        tree[leaf] = None

        return cnt

    return bst_helper(list(range(1, n + 1)), [], True)



import pytest


@pytest.mark.parametrize("n, expected", [
    # (1, 1),
    # (2, 2),
    (3, 5),
])
def test_bst(n, expected):
    assert(how_many_BSTs(n)) == expected


pytest.main()
