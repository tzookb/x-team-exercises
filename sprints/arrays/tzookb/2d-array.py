def hourglassSum(arr):
    res = []
    res.append(get_single_hourglassSum(0, 0, arr))
    res.append(get_single_hourglassSum(1, 0, arr))
    res.append(get_single_hourglassSum(2, 0, arr))
    res.append(get_single_hourglassSum(3, 0, arr))
    
    res.append(get_single_hourglassSum(0, 1, arr))
    res.append(get_single_hourglassSum(1, 1, arr))
    res.append(get_single_hourglassSum(2, 1, arr))
    res.append(get_single_hourglassSum(3, 1, arr))

    res.append(get_single_hourglassSum(0, 2, arr))
    res.append(get_single_hourglassSum(1, 2, arr))
    res.append(get_single_hourglassSum(2, 2, arr))
    res.append(get_single_hourglassSum(3, 2, arr))

    res.append(get_single_hourglassSum(0, 3, arr))
    res.append(get_single_hourglassSum(1, 3, arr))
    res.append(get_single_hourglassSum(2, 3, arr))
    res.append(get_single_hourglassSum(3, 3, arr))

    print(max(res))
    

def get_single_hourglassSum(x, y, arr):
    items = [
        arr[y][x],
        arr[y][x+1],
        arr[y][x+2],
        arr[y+1][x+1],
        arr[y+2][x],
        arr[y+2][x+1],
        arr[y+2][x+2],
    ]
    return sum(items)

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
    
result = hourglassSum(arr)