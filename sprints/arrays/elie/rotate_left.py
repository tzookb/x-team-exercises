#!/bin/python

import os


def rotate_left(arr, d):
    return arr[d:] + arr[:d]
    

if __name__ == '__main__':
    readline = lambda: map(int, raw_input().rstrip().split())
    (_, d), arr = readline(), readline()
    res = rotate_left(arr, d)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
