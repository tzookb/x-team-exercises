# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem


def sherlock(string):
    n = len(string)
    hash = {}

    for i in xrange(0, n):
        for j in xrange(i + 1, n + 1):
            substring = [s for s in string[i:j]]
            substring = ''.join(sorted(substring))
            hash[substring] = hash.get(substring, 0) + 1    

    return sum([v * (v - 1) / 2 for v in hash.values()])


if __name__ == '__main__':
    q = int(raw_input())
    for _ in xrange(q):
        string = raw_input()
        print sherlock(string)
