def find_integer(arr):
    # 1. Bucketized counts
    bucket_bits = 16
    bucket_size = 2 ** bucket_bits
    bucket_count = 2 ** (32 - bucket_bits)
    buckets = [0] * bucket_count
    for a in arr:
        i = a // bucket_size
        buckets[i] += 1

    # 2. Pick a bucket
    b = 0
    for bucket in buckets:
        if bucket < bucket_size:
            break

        b += 1

    # We assume 64 bit integers
    # import sys
    # print(sys.maxsize)
    # 64 -> 6 bits

    # 3. Iterate again and focus on that bucket
    diff_bits = 6
    diff = 2 ** diff_bits
    bits = bucket_bits - diff_bits
    aux = [0] * (2 ** bits)
    filled = 2 ** diff - 1
    counter = 0
    for a in arr:
        i1 = a // bucket_size
        if i1 == b:
            a2 = a % bucket_size
            i2 = a2 // diff
            r = a2 % diff
            flag = 1 << r
            aux[i2] |= flag
            counter += 1
            # If we reached that bucket count we can stop
            if counter == buckets[b]:
                break

    # 4. Find the lowest bit flag in the bucket
    i = 0
    base = b * bucket_size
    for a in aux:
        if a < filled:
            k = 0
            while a > 0:
                if a % 2 == 0:
                    return base + k

                a //= 2
                k += 1

            return base + k

        base += diff
        i += 1

    return -1

