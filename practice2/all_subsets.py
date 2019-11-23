def generate_all_subsets(s):
    length = len(s)
    result = []

    def gen_helper(problem, partial):
        if len(problem) == 0:
            result.append(partial)
            return

        pr = problem[1:]
        gen_helper(pr, partial)
        gen_helper(pr, partial + problem[0])

    gen_helper(s, "")

    return result
