def left_rotate(arr, n):
    size_of_arr = len(arr)
    extra_moves = n % size_of_arr

    return arr[extra_moves:] + arr[:extra_moves]

res = left_rotate([1,2,3,4,5], 2)

print(" ".join(str(x) for x in res))