def minimumSwaps(arr):
    counter = 0
    sorted = arr[:]
    sorted.sort()
    for idx, num in enumerate(arr):
        if sorted[idx] != num:
            counter += 1
    return counter-1

# not good!
res = minimumSwaps([1, 3, 5, 2, 4, 6, 8])
print(res)