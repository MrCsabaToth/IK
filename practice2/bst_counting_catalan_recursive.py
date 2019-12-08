def how_many_BSTs(n):
    def bst_count_helper(k):
        if k == 0:
            return 1
    
        return (4 * (k - 1) + 2) / (k + 1) * how_many_BSTs(k - 1)

    return int(bst_count_helper(n))
