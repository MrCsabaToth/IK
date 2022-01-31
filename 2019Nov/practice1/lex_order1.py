def solve(arr):
    dic = dict()
    for item in arr:
        keyval = item.split(" ")

        if keyval[0] not in dic:
            dic[keyval[0]] = [keyval[1]]
        else:
            dic[keyval[0]].append(keyval[1])

    return ["{}:{},{}".format(kv[0], len(kv[1]), sorted(kv[1])[-1]) for kv in dic.items()]
