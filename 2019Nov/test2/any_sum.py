def check_if_sum_possible(arr, k):
    length = len(arr)

    def sum_helper(partial, idx):
        if partial == k:
            return True

        if idx > length - 1:
            return False

        # We rely on Python: it won't execute the second expression if the first is already True in an or
        # This is a backtrack as well: we backtrack from the second, the traversal won't touch that branch
        return (
            sum_helper(partial, idx + 1) or
            sum_helper((partial if partial is not None else 0) + arr[idx], idx + 1)
        )

    # The fact that we can have negative integers in the arr
    # means that we cannot have some early backtrack criteria
    # We need to traverse the full permutation until we find
    # one solution. In that case we can return True
    return sum_helper(None, 0)
