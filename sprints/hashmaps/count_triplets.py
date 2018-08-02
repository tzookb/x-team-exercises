# https://www.hackerrank.com/challenges/count-triplets-1/problem


def count_triplets(r, numbers):  
    hash1 = {}
    hash2 = {}
    count = 0

    for x in reversed(numbers):
        count += hash1.get(x * r, 0)
        hash1[x] = hash1.get(x, 0) + hash2.get(x * r, 0)
        hash2[x] = hash2.get(x, 0) + 1

    return count


if __name__ == '__main__':
    readline = lambda: map(int, raw_input().rstrip().split())
    _, r = readline()
    numbers = readline()
    print count_triplets(r, numbers)
