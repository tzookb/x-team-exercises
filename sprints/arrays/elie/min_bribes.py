#!/bin/python


def min_bribes(n, q):
    for i, j in enumerate(q):
        if j > i + 3:
            return 'Too chaotic'

    count = 0
    while True:
        prev = 0
        for i in xrange(prev, n - 1):
            if q[i] > q[i + 1]:
                q[i], q[i + 1] = q[i + 1], q[i]
                count += 1
                prev = i

        if not prev:
            break

    return count


if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        n = int(raw_input())
        q = map(int, raw_input().rstrip().split())
        print min_bribes(n, q)
