def solve(arr):
    sol = dict()
    for elem in arr:
        vals = elem.split(" ")
        if vals[0] not in sol:
            sol[vals[0]] = [1, vals[1]]
        else:
            entry = sol[vals[0]]
            entry[0] += 1
            if entry[1] < vals[1]:
                entry[1] = vals[1]

    return ["{}:{},{}".format(key, val[0], val[1]) for key,val in iter(sol.items())]
