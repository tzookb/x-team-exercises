import math

def median_from_dict(dict):
    total = sum(dict.values())
    if total == 0:
        return 0
    
    if total == 1:
        only_key = next(iter(dict)) 
        return dict[only_key]

    half = math.floor(total/2)
    is_single_for_median = total%2 == 1
    till_now = 0

    for key in sorted(dict.iterkeys()):
        current_amount = dict[key]
        if till_now + current_amount <= half:
            if (is_single_for_median):
                return key
            else:
                pass

    return total

def median(a,x):
    holder = {}

    for idx, action in enumerate(a):
        number = x[idx]
        if action == 'r':
            if number in holder:
                del holder[number]
            else:
                print("Wrong!")
        else:
            if number not in holder:
                holder[number] = 0
            holder[number] += 1
            median_res = median_from_dict(holder)
            print(median_res)

a = ['r', 'a', 'a', 'a', 'r', 'r', 'r']
x = [1, 1, 2, 1, 1, 2, 1]
# median(a,x)

res = median_from_dict({
    1: 2,
    2: 1 
})
print(res)