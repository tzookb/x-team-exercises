#!/bin/python

import os


def min_swaps(arr):
    n = len(arr)
    count = 0
    done = False
    
    while not done:
        done = True

        for i in xrange(n):
            v = arr[i] - 1
            v = min(n - 1, v)  # don't really need this but TC14 is broken
            if v != i:
                arr[v], arr[i] = arr[i], arr[v]
                done = False
                count += 1

    return count
    

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())
    res = min_swaps(arr)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(res) + '\n')
    fptr.close()
