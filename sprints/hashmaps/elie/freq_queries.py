# https://www.hackerrank.com/challenges/frequency-queries/problem


def freq_queries(queries):
    result = []
    hash1 = {}
    hash2 = {}

    for op, i in queries:
        if op == 3:
            result.append(1 if hash2.get(i, 0) > 0 else 0)
            continue

        c = hash1.get(i, 0)
        d = c + 1 if op == 1 else c - 1

        hash1[i] = max(0, d)
        hash2[c] = max(0, hash2.get(c, 0) - 1)
        hash2[d] = max(0, hash2.get(d, 0) + 1)

    return result


if __name__ == '__main__':
    readline = lambda: map(int, raw_input().rstrip().split())
    q = readline()[0]
    queries = [readline() for _ in range(q)]
    result = freq_queries(queries)
    for r in result:
        print r
