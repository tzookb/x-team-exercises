import math

def repeatedString(s, n):
    str_len = len(s)
    mult_times = math.floor(n/str_len)
    remainder = n%str_len
    total_a_in_str_global = list(s).count('a')
    
    total_a_in_str_remainder = list(s)[:remainder].count('a')
    return int(total_a_in_str_global*mult_times + total_a_in_str_remainder)

res = repeatedString('aba',10)
print(res)