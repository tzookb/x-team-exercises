#!/bin/python

import os


def array_manipulation(n, queries):
    arr = [0] * (n + 2)
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    max = 0
    val = 0
    for v in arr:
        val += v
        if val > max:
            max = val

    return max


if __name__ == '__main__':
    readline = lambda: map(int, raw_input().rstrip().split())
    n, m = readline()
    queries = [readline() for _ in xrange(m)]
    result = array_manipulation(n, queries)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
