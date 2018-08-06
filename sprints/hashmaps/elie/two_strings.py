# https://www.hackerrank.com/challenges/two-strings/problem


def two_strings(s1, s2):
    hash = {s: True for s in s1}
    for s in s2:
        if hash.get(s):
            return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    q = int(raw_input())
    for _ in xrange(q):
        s1 = raw_input()
        s2 = raw_input()
        print two_strings(s1, s2)
