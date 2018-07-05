# from __future__ import division

def get_median(sorted_nums):
    items_len = len(sorted_nums)
    if items_len == 1:
        return sorted_nums[0]
    
    items_len_middle = items_len/2 
    if items_len%2 == 0:
        return (float(sorted_nums[items_len_middle-1]) + float(sorted_nums[items_len_middle]))/2
    else:
        return sorted_nums[items_len_middle]

print(get_median([1]))
print(get_median([1,2]))
print(get_median([1,2,3]))