readline = lambda: int(raw_input().strip())

n = readline()
rank = [readline() for i in xrange(n)]
candies = [1] * n
count = n

for i in xrange(n):
    j = n - i - 1

    if i > 0 and rank[i] > rank[i - 1] and candies[i] <= candies[i - 1]:
        delta = candies[i - 1] - candies[i] + 1
        count += delta
        candies[i] += delta

    if i < n - 1 and rank[i] > rank[i + 1] and candies[i] <= candies[i + 1]:
        delta = candies[i + 1] - candies[i] + 1
        count += delta
        candies[i] += delta

    if j > 0 and rank[j] > rank[j - 1] and candies[j] <= candies[j - 1]:
        delta = candies[j - 1] - candies[j] + 1
        count += delta
        candies[j] += delta

    if j < n - 1 and rank[j] > rank[j + 1] and candies[j] <= candies[j + 1]:
        delta = candies[j + 1] - candies[j] + 1
        count += delta
        candies[j] += delta

print count