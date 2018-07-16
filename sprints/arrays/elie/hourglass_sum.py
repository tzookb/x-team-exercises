#!/bin/python

import os


def hourglass_sum(arr):
    n = len(arr) - 2
    m = None

    for i in xrange(n):
        for j in xrange(n):
            s = (
                arr[i][j] +
                arr[i][j + 1] +
                arr[i][j + 2] +
                arr[i + 1][j + 1] +
                arr[i + 2][j] +
                arr[i + 2][j + 1] +
                arr[i + 2][j + 2]
            )

            if m is None or s > m:
                m = s

    return m


if __name__ == '__main__':
    readline = lambda: map(int, raw_input().rstrip().split())
    arr = [readline() for _ in xrange(6)]
    res = hourglass_sum(arr)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(res) + '\n')
    fptr.close()
