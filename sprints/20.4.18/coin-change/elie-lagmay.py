readline = lambda: map(int, raw_input().strip().split(' '))

n, m = readline()
coins = readline()

ways = [1] + [0] * n

for c in coins:
    for i in xrange(c, n + 1):
        ways[i] += ways[i - c]

print ways[n]