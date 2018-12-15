def matchingStrings(strings, queries):
    counts = {}
    result = []
    for item in strings:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    
    for query in queries:
        if query in counts:
            result.append(counts[query])
        else:
            result.append(0)

    return result

res = matchingStrings(
    ['ab', 'ab', 'abc'],
    ['ab', 'abc', 'bc']
)
print(res)