# https://www.hackerrank.com/challenges/ctci-ransom-note/problem


def ransom(magazine, note):
    hash = {}

    for word in magazine:
        hash[word] = hash.get(word, 0) + 1

    for word in note:
        hash[word] = hash.get(word, 0) - 1
        if hash[word] < 0:
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    readline = lambda: raw_input().rstrip().split()
    _ = readline()
    magazine = readline()
    note = readline()
    print ransom(magazine, note)
